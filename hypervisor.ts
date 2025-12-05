/**
 * 🔒 HYPERVISOR
 * Safe execution environment for all NoizyOS processes
 * Fish Music Inc - CB_01
 */

export interface Task {
  id: string;
  name: string;
  execute: () => any;
  rollback?: () => void;
}

class Hypervisor {
  private runningTasks: Map<string, Task> = new Map();

  init() {
    console.log('🔒 Hypervisor initialized');
  }

  async run(task: Task): Promise<any> {
    console.log(`🔒 Hypervisor executing: ${task.name}`);
    
    this.runningTasks.set(task.id, task);

    try {
      const result = await task.execute();
      
      console.log(`   ✅ Task completed: ${task.name}`);
      this.runningTasks.delete(task.id);
      
      return {
        success: true,
        result,
        task_id: task.id
      };

    } catch (error) {
      console.error(`   ❌ Task failed: ${task.name}`, error);
      
      // Attempt rollback
      if (task.rollback) {
        console.log(`   ⏮️  Rolling back: ${task.name}`);
        try {
          task.rollback();
          console.log('   ✅ Rollback successful');
        } catch (rollbackError) {
          console.error('   ❌ Rollback failed:', rollbackError);
        }
      }

      this.runningTasks.delete(task.id);
      
      return {
        success: false,
        error: error instanceof Error ? error.message : 'Unknown error',
        task_id: task.id
      };
    }
  }

  getRunningTasks() {
    return Array.from(this.runningTasks.values());
  }

  killTask(taskId: string) {
    console.log(`🛑 Killing task: ${taskId}`);
    this.runningTasks.delete(taskId);
  }
}

export const hypervisor = new Hypervisor();
