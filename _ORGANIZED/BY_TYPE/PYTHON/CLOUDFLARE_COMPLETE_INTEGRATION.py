#!/usr/bin/env python3
"""
🚀 CLOUDFLARE COMPLETE INTEGRATION - FISH MUSIC INC
Deploy webhooks, workers, R2 storage, email routing - ALL FREE!
"""

import requests
import json
import os
from datetime import datetime

class CloudflareIntegration:
    """Complete Cloudflare integration for Fish Music"""
    
    def __init__(self, api_token=None, account_id=None):
        self.api_token = api_token or os.getenv('CLOUDFLARE_API_TOKEN')
        self.account_id = account_id or os.getenv('CLOUDFLARE_ACCOUNT_ID')
        self.base_url = "https://api.cloudflare.com/client/v4"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
    
    # CLOUDFLARE WORKERS - DEPLOY WEBHOOKS
    
    def create_worker_webhook(self, worker_name, script_content):
        """Deploy a Cloudflare Worker (serverless function)"""
        url = f"{self.base_url}/accounts/{self.account_id}/workers/scripts/{worker_name}"
        
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/javascript'
        
        response = requests.put(url, headers=headers, data=script_content)
        
        if response.status_code == 200:
            print(f"✅ Worker deployed: {worker_name}")
            print(f"   URL: https://{worker_name}.{self.account_id}.workers.dev")
            return True
        else:
            print(f"❌ Worker deployment failed: {response.text}")
            return False
    
    def get_stripe_webhook_worker(self):
        """Generate Cloudflare Worker code for Stripe webhook"""
        return """
// 🐟 Fish Music Stripe Webhook Worker
export default {
  async fetch(request, env) {
    if (request.method !== 'POST') {
      return new Response('Method not allowed', { status: 405 });
    }
    
    try {
      const event = await request.json();
      
      // Handle payment success
      if (event.type === 'payment_intent.succeeded') {
        const customerEmail = event.data.object.receipt_email;
        const amount = event.data.object.amount / 100;
        const orderId = event.data.object.id;
        
        // Send email via our system
        await fetch('https://email.fishmusicinc.com/send-receipt', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: customerEmail,
            amount: amount,
            order_id: orderId
          })
        });
        
        return new Response(JSON.stringify({ success: true }), {
          headers: { 'Content-Type': 'application/json' }
        });
      }
      
      return new Response(JSON.stringify({ received: true }), {
        headers: { 'Content-Type': 'application/json' }
      });
      
    } catch (error) {
      return new Response(JSON.stringify({ error: error.message }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }
  }
};
"""
    
    # CLOUDFLARE R2 - STORAGE FOR TRACKS
    
    def create_r2_bucket(self, bucket_name):
        """Create R2 bucket for track storage"""
        url = f"{self.base_url}/accounts/{self.account_id}/r2/buckets"
        
        data = {"name": bucket_name}
        
        response = requests.post(url, headers=self.headers, json=data)
        
        if response.status_code == 200:
            print(f"✅ R2 bucket created: {bucket_name}")
            return True
        else:
            print(f"❌ Bucket creation failed: {response.text}")
            return False
    
    def upload_to_r2(self, bucket_name, file_path, object_name=None):
        """Upload file to R2 bucket"""
        if object_name is None:
            object_name = os.path.basename(file_path)
        
        # Generate presigned URL (requires R2 credentials)
        print(f"📤 Uploading {file_path} to R2 bucket {bucket_name}")
        print(f"   Use R2 API or S3-compatible client for actual upload")
        
        return True
    
    # CLOUDFLARE DNS - EMAIL & DOMAIN
    
    def setup_email_routing(self, domain, destination_email):
        """Setup Cloudflare Email Routing"""
        zone_id = self.get_zone_id(domain)
        
        url = f"{self.base_url}/zones/{zone_id}/email/routing/rules"
        
        data = {
            "actions": [{
                "type": "forward",
                "value": [destination_email]
            }],
            "matchers": [{
                "type": "all"
            }],
            "name": f"Forward all to {destination_email}",
            "enabled": True
        }
        
        response = requests.post(url, headers=self.headers, json=data)
        
        if response.status_code == 200:
            print(f"✅ Email routing configured for {domain}")
            print(f"   All emails → {destination_email}")
            return True
        else:
            print(f"❌ Email routing failed: {response.text}")
            return False
    
    def get_zone_id(self, domain):
        """Get zone ID for domain"""
        url = f"{self.base_url}/zones?name={domain}"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            zones = response.json()['result']
            if zones:
                return zones[0]['id']
        
        return None
    
    # CLOUDFLARE AI - AI MODELS AT EDGE
    
    def run_ai_model(self, model_name, inputs):
        """Run Cloudflare AI model"""
        url = f"{self.base_url}/accounts/{self.account_id}/ai/run/{model_name}"
        
        response = requests.post(url, headers=self.headers, json=inputs)
        
        if response.status_code == 200:
            return response.json()['result']
        else:
            print(f"❌ AI model failed: {response.text}")
            return None
    
    def generate_track_description(self, track_name, genre):
        """Generate AI description for track"""
        return self.run_ai_model(
            "@cf/meta/llama-2-7b-chat-int8",
            {
                "messages": [{
                    "role": "user",
                    "content": f"Write a compelling 2-sentence description for a {genre} music track called '{track_name}'"
                }]
            }
        )
    
    def generate_email_subject(self, context):
        """Generate AI email subject line"""
        return self.run_ai_model(
            "@cf/meta/llama-2-7b-chat-int8",
            {
                "messages": [{
                    "role": "user",
                    "content": f"Write a catchy email subject line for: {context}"
                }]
            }
        )

# CLI INTERFACE
if __name__ == "__main__":
    import sys
    
    print("🚀 CLOUDFLARE COMPLETE INTEGRATION")
    print("=" * 60)
    print()
    
    if len(sys.argv) < 2:
        print("""
USAGE:
  Deploy Stripe webhook worker:
    python3 CLOUDFLARE_COMPLETE_INTEGRATION.py deploy-stripe
  
  Create R2 bucket:
    python3 CLOUDFLARE_COMPLETE_INTEGRATION.py create-bucket fish-music-tracks
  
  Setup email routing:
    python3 CLOUDFLARE_COMPLETE_INTEGRATION.py setup-email fishmusicinc.com rsp@noizyfish.com
  
  Generate track description:
    python3 CLOUDFLARE_COMPLETE_INTEGRATION.py describe "Track Name" "Genre"

SETUP:
  1. Get Cloudflare API token: https://dash.cloudflare.com/profile/api-tokens
  2. Set environment variables:
     export CLOUDFLARE_API_TOKEN="your_token"
     export CLOUDFLARE_ACCOUNT_ID="your_account_id"
        """)
        sys.exit(0)
    
    cf = CloudflareIntegration()
    command = sys.argv[1]
    
    if command == "deploy-stripe":
        worker_script = cf.get_stripe_webhook_worker()
        cf.create_worker_webhook("fish-music-stripe-webhook", worker_script)
    
    elif command == "create-bucket":
        bucket_name = sys.argv[2]
        cf.create_r2_bucket(bucket_name)
    
    elif command == "setup-email":
        domain = sys.argv[2]
        destination = sys.argv[3]
        cf.setup_email_routing(domain, destination)
    
    elif command == "describe":
        track = sys.argv[2]
        genre = sys.argv[3]
        result = cf.generate_track_description(track, genre)
        print(f"\n🎵 AI Description:\n{result}")
    
    else:
        print(f"❌ Unknown command: {command}")

