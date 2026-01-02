#!/usr/bin/env python3
"""
Agent Communication Protocol (ACP)
Enables agents to communicate with each other and external systems
"""
import json
import asyncio
import time
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass, field, asdict
from enum import Enum
import logging

logger = logging.getLogger("ACP")

class MessageType(Enum):
    """Types of messages agents can send"""
    TASK_REQUEST = "task_request"
    TASK_RESPONSE = "task_response"
    STATUS_UPDATE = "status_update"
    AGENT_DISCOVERY = "agent_discovery"
    RESOURCE_REQUEST = "resource_request"
    ALERT = "alert"
    HEARTBEAT = "heartbeat"
    BROADCAST = "broadcast"

class MessagePriority(Enum):
    """Message priority levels"""
    CRITICAL = 0
    HIGH = 1
    NORMAL = 2
    LOW = 3

@dataclass
class Message:
    """Communication message between agents"""
    msg_id: str
    msg_type: MessageType
    sender: str
    recipient: str  # Use "*" for broadcast
    payload: Dict[str, Any]
    priority: MessagePriority = MessagePriority.NORMAL
    timestamp: float = field(default_factory=time.time)
    requires_response: bool = False
    correlation_id: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert message to dictionary"""
        data = asdict(self)
        data['msg_type'] = self.msg_type.value
        data['priority'] = self.priority.value
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Message':
        """Create message from dictionary"""
        data['msg_type'] = MessageType(data['msg_type'])
        data['priority'] = MessagePriority(data['priority'])
        return cls(**data)

class MessageBus:
    """Central message bus for agent communication"""
    
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}
        self.message_history: List[Message] = []
        self.max_history = 1000
        self.logger = logging.getLogger("MessageBus")
    
    def subscribe(self, agent_id: str, callback: Callable):
        """Subscribe an agent to receive messages"""
        if agent_id not in self.subscribers:
            self.subscribers[agent_id] = []
        self.subscribers[agent_id].append(callback)
        self.logger.info(f"📡 {agent_id} subscribed to message bus")
    
    def unsubscribe(self, agent_id: str):
        """Unsubscribe an agent from messages"""
        if agent_id in self.subscribers:
            del self.subscribers[agent_id]
            self.logger.info(f"📡 {agent_id} unsubscribed from message bus")
    
    async def publish(self, message: Message):
        """Publish a message to the bus"""
        self.message_history.append(message)
        
        # Trim history if needed
        if len(self.message_history) > self.max_history:
            self.message_history = self.message_history[-self.max_history:]
        
        # Determine recipients
        if message.recipient == "*":
            # Broadcast to all
            recipients = list(self.subscribers.keys())
        else:
            recipients = [message.recipient] if message.recipient in self.subscribers else []
        
        # Deliver message
        for recipient in recipients:
            if recipient in self.subscribers:
                for callback in self.subscribers[recipient]:
                    try:
                        if asyncio.iscoroutinefunction(callback):
                            await callback(message)
                        else:
                            callback(message)
                    except Exception as e:
                        self.logger.error(f"Error delivering message to {recipient}: {e}")
        
        self.logger.debug(f"📤 Message {message.msg_id} delivered to {len(recipients)} recipients")
    
    def get_history(self, agent_id: Optional[str] = None, limit: int = 100) -> List[Message]:
        """Get message history, optionally filtered by agent"""
        messages = self.message_history
        
        if agent_id:
            messages = [
                m for m in messages
                if m.sender == agent_id or m.recipient == agent_id or m.recipient == "*"
            ]
        
        return messages[-limit:]

class AgentCommunicator:
    """Handles communication for an individual agent"""
    
    def __init__(self, agent_id: str, message_bus: MessageBus):
        self.agent_id = agent_id
        self.message_bus = message_bus
        self.pending_responses: Dict[str, asyncio.Future] = {}
        self.logger = logging.getLogger(f"Communicator.{agent_id}")
        
        # Subscribe to message bus
        self.message_bus.subscribe(agent_id, self._handle_message)
    
    async def send_message(
        self,
        recipient: str,
        msg_type: MessageType,
        payload: Dict[str, Any],
        priority: MessagePriority = MessagePriority.NORMAL,
        wait_for_response: bool = False
    ) -> Optional[Message]:
        """Send a message to another agent"""
        msg_id = f"{self.agent_id}_{int(time.time() * 1000)}"
        
        message = Message(
            msg_id=msg_id,
            msg_type=msg_type,
            sender=self.agent_id,
            recipient=recipient,
            payload=payload,
            priority=priority,
            requires_response=wait_for_response
        )
        
        if wait_for_response:
            # Create a future for the response
            future = asyncio.Future()
            self.pending_responses[msg_id] = future
        
        await self.message_bus.publish(message)
        self.logger.info(f"📤 Sent {msg_type.value} to {recipient}")
        
        if wait_for_response:
            try:
                response = await asyncio.wait_for(future, timeout=5.0)
                return response
            except asyncio.TimeoutError:
                self.logger.warning(f"⏰ Response timeout for message {msg_id}")
                del self.pending_responses[msg_id]
                return None
        
        return None
    
    async def broadcast(
        self,
        msg_type: MessageType,
        payload: Dict[str, Any],
        priority: MessagePriority = MessagePriority.NORMAL
    ):
        """Broadcast a message to all agents"""
        await self.send_message("*", msg_type, payload, priority)
        self.logger.info(f"📢 Broadcast {msg_type.value} to all agents")
    
    async def _handle_message(self, message: Message):
        """Handle incoming messages"""
        self.logger.debug(f"📥 Received {message.msg_type.value} from {message.sender}")
        
        # Check if this is a response to a pending request
        if message.correlation_id and message.correlation_id in self.pending_responses:
            future = self.pending_responses.pop(message.correlation_id)
            if not future.done():
                future.set_result(message)
        
        # Handle specific message types
        if message.msg_type == MessageType.TASK_REQUEST:
            await self._handle_task_request(message)
        elif message.msg_type == MessageType.STATUS_UPDATE:
            await self._handle_status_update(message)
        elif message.msg_type == MessageType.AGENT_DISCOVERY:
            await self._handle_agent_discovery(message)
    
    async def _handle_task_request(self, message: Message):
        """Handle task request from another agent"""
        self.logger.info(f"📋 Task request received from {message.sender}")
        # Agent-specific handling would go here
    
    async def _handle_status_update(self, message: Message):
        """Handle status update from another agent"""
        self.logger.debug(f"📊 Status update from {message.sender}")
    
    async def _handle_agent_discovery(self, message: Message):
        """Handle agent discovery message"""
        self.logger.info(f"🔍 Agent discovery from {message.sender}")
    
    def disconnect(self):
        """Disconnect from message bus"""
        self.message_bus.unsubscribe(self.agent_id)
        self.logger.info("📡 Disconnected from message bus")

# Global message bus instance
global_message_bus = MessageBus()

def get_communicator(agent_id: str) -> AgentCommunicator:
    """Get a communicator for an agent"""
    return AgentCommunicator(agent_id, global_message_bus)

if __name__ == "__main__":
    print("📡 Agent Communication Protocol (ACP)")
    print("Message bus initialized and ready for agent communication")
