/**
 * ████ NOIZYLAB TRAINING SIMULATOR ████
 * 
 * VIRTUAL REPAIR TRAINING WITH GAMIFICATION
 * - Interactive repair simulations
 * - Skill-based progression system
 * - Achievement badges and certifications
 * - Timed challenges
 * - Error scenarios and troubleshooting
 * - Leaderboards and competitions
 * - AI-powered skill assessment
 */

export interface Env {
  DB: D1Database;
  TRAINING_KV: KVNamespace;
  AI: Ai;
  BRAIN: Fetcher;
}

interface TrainingModule {
  id: string;
  title: string;
  description: string;
  device_category: string;
  difficulty: 'beginner' | 'intermediate' | 'advanced' | 'expert';
  skill_points: number;
  estimated_minutes: number;
  prerequisites: string[];
  lessons: TrainingLesson[];
  final_exam: Exam;
  certification: Certification | null;
}

interface TrainingLesson {
  id: string;
  title: string;
  type: 'video' | 'interactive' | 'quiz' | 'simulation';
  content: any;
  skill_points: number;
  required_score: number;
}

interface Simulation {
  id: string;
  name: string;
  device_type: string;
  scenario: string;
  initial_state: DeviceState;
  target_state: DeviceState;
  available_tools: string[];
  available_parts: string[];
  time_limit_seconds: number;
  hints: SimulationHint[];
  scoring: ScoringRules;
}

interface DeviceState {
  components: Record<string, ComponentState>;
  connections: Connection[];
  power_on: boolean;
  symptoms: string[];
}

interface ComponentState {
  id: string;
  name: string;
  position: { x: number; y: number };
  condition: 'good' | 'damaged' | 'missing' | 'wrong';
  installed: boolean;
}

interface Connection {
  from: string;
  to: string;
  type: 'ribbon' | 'wire' | 'flex' | 'solder';
  connected: boolean;
}

interface SimulationHint {
  trigger: string;
  message: string;
  penalty_points: number;
}

interface ScoringRules {
  time_bonus_threshold: number;
  time_bonus_points: number;
  no_hints_bonus: number;
  first_try_bonus: number;
  penalty_per_mistake: number;
}

interface Exam {
  id: string;
  questions: ExamQuestion[];
  passing_score: number;
  time_limit_minutes: number;
}

interface ExamQuestion {
  id: string;
  type: 'multiple_choice' | 'true_false' | 'image_identify' | 'order_steps';
  question: string;
  options?: string[];
  correct_answer: string | string[];
  points: number;
  explanation: string;
}

interface Certification {
  id: string;
  name: string;
  description: string;
  valid_months: number;
  badge_url: string;
}

interface UserProgress {
  user_id: string;
  total_xp: number;
  level: number;
  modules_completed: string[];
  certifications: string[];
  achievements: string[];
  current_streak: number;
  longest_streak: number;
  skills: Record<string, number>;
}

interface Achievement {
  id: string;
  name: string;
  description: string;
  icon: string;
  xp_reward: number;
  rarity: 'common' | 'uncommon' | 'rare' | 'epic' | 'legendary';
  condition: AchievementCondition;
}

interface AchievementCondition {
  type: 'count' | 'streak' | 'score' | 'time' | 'special';
  target: number;
  metric: string;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const path = url.pathname;

    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        },
      });
    }

    try {
      // === TRAINING MODULES ===
      if (path === '/modules' && request.method === 'GET') {
        return this.listModules(url, env);
      }

      if (path.match(/^\/modules\/[^/]+$/) && request.method === 'GET') {
        const moduleId = path.split('/')[2];
        return this.getModule(moduleId, env);
      }

      if (path.match(/^\/modules\/[^/]+\/start$/) && request.method === 'POST') {
        const moduleId = path.split('/')[2];
        return this.startModule(moduleId, request, env);
      }

      // === SIMULATIONS ===
      if (path === '/simulations' && request.method === 'GET') {
        return this.listSimulations(url, env);
      }

      if (path.match(/^\/simulations\/[^/]+\/start$/) && request.method === 'POST') {
        const simId = path.split('/')[2];
        return this.startSimulation(simId, request, env);
      }

      if (path.match(/^\/simulations\/[^/]+\/action$/) && request.method === 'POST') {
        const simId = path.split('/')[2];
        return this.performAction(simId, request, env);
      }

      if (path.match(/^\/simulations\/[^/]+\/hint$/) && request.method === 'GET') {
        const simId = path.split('/')[2];
        return this.getHint(simId, url, env);
      }

      if (path.match(/^\/simulations\/[^/]+\/complete$/) && request.method === 'POST') {
        const simId = path.split('/')[2];
        return this.completeSimulation(simId, request, env);
      }

      // === EXAMS ===
      if (path.match(/^\/exams\/[^/]+\/start$/) && request.method === 'POST') {
        const examId = path.split('/')[2];
        return this.startExam(examId, request, env);
      }

      if (path.match(/^\/exams\/[^/]+\/submit$/) && request.method === 'POST') {
        const examId = path.split('/')[2];
        return this.submitExam(examId, request, env);
      }

      // === USER PROGRESS ===
      if (path === '/progress' && request.method === 'GET') {
        return this.getProgress(url, env);
      }

      if (path === '/progress/skills' && request.method === 'GET') {
        return this.getSkillTree(url, env);
      }

      // === ACHIEVEMENTS ===
      if (path === '/achievements' && request.method === 'GET') {
        return this.getAchievements(url, env);
      }

      if (path.match(/^\/achievements\/[^/]+\/claim$/) && request.method === 'POST') {
        const achievementId = path.split('/')[2];
        return this.claimAchievement(achievementId, request, env);
      }

      // === CERTIFICATIONS ===
      if (path === '/certifications' && request.method === 'GET') {
        return this.getCertifications(url, env);
      }

      if (path.match(/^\/certifications\/[^/]+\/verify$/) && request.method === 'GET') {
        const certId = path.split('/')[2];
        return this.verifyCertification(certId, env);
      }

      // === LEADERBOARDS ===
      if (path === '/leaderboard' && request.method === 'GET') {
        return this.getLeaderboard(url, env);
      }

      if (path === '/leaderboard/weekly' && request.method === 'GET') {
        return this.getWeeklyLeaderboard(env);
      }

      // === CHALLENGES ===
      if (path === '/challenges/daily' && request.method === 'GET') {
        return this.getDailyChallenge(env);
      }

      if (path === '/challenges/weekly' && request.method === 'GET') {
        return this.getWeeklyChallenge(env);
      }

      if (path.match(/^\/challenges\/[^/]+\/submit$/) && request.method === 'POST') {
        const challengeId = path.split('/')[2];
        return this.submitChallenge(challengeId, request, env);
      }

      // === AI ASSESSMENT ===
      if (path === '/assess/skill' && request.method === 'POST') {
        return this.assessSkill(request, env);
      }

      if (path === '/assess/weakness' && request.method === 'GET') {
        return this.identifyWeaknesses(url, env);
      }

      if (path === '/recommend' && request.method === 'GET') {
        return this.getRecommendations(url, env);
      }

      return this.jsonResponse({ error: 'Not found' }, 404);
    } catch (error) {
      console.error('Training error:', error);
      return this.jsonResponse({ error: 'Internal error' }, 500);
    }
  },

  // === TRAINING MODULES ===
  async listModules(url: URL, env: Env): Promise<Response> {
    const category = url.searchParams.get('category');
    const difficulty = url.searchParams.get('difficulty');
    const userId = url.searchParams.get('user_id');

    let query = 'SELECT * FROM training_modules WHERE 1=1';
    const params: any[] = [];

    if (category) {
      query += ' AND device_category = ?';
      params.push(category);
    }
    if (difficulty) {
      query += ' AND difficulty = ?';
      params.push(difficulty);
    }

    query += ' ORDER BY skill_points ASC';

    const modules = await env.DB.prepare(query).bind(...params).all();

    // Get user progress if user_id provided
    let userProgress: any = null;
    if (userId) {
      userProgress = await env.DB.prepare(
        'SELECT modules_completed FROM user_training_progress WHERE user_id = ?'
      ).bind(userId).first();
    }

    const completedModules = userProgress 
      ? JSON.parse(userProgress.modules_completed || '[]') 
      : [];

    const enriched = (modules.results || []).map((mod: any) => ({
      ...mod,
      lessons: JSON.parse(mod.lessons || '[]'),
      prerequisites: JSON.parse(mod.prerequisites || '[]'),
      completed: completedModules.includes(mod.id),
      unlocked: this.checkPrerequisites(JSON.parse(mod.prerequisites || '[]'), completedModules),
    }));

    return this.jsonResponse({
      modules: enriched,
      total: enriched.length,
    });
  },

  checkPrerequisites(prereqs: string[], completed: string[]): boolean {
    return prereqs.every(p => completed.includes(p));
  },

  async getModule(moduleId: string, env: Env): Promise<Response> {
    const module = await env.DB.prepare(
      'SELECT * FROM training_modules WHERE id = ?'
    ).bind(moduleId).first() as any;

    if (!module) {
      return this.jsonResponse({ error: 'Module not found' }, 404);
    }

    return this.jsonResponse({
      ...module,
      lessons: JSON.parse(module.lessons || '[]'),
      prerequisites: JSON.parse(module.prerequisites || '[]'),
      final_exam: JSON.parse(module.final_exam || '{}'),
      certification: JSON.parse(module.certification || 'null'),
    });
  },

  async startModule(moduleId: string, request: Request, env: Env): Promise<Response> {
    const { user_id } = await request.json() as any;

    // Check prerequisites
    const module = await env.DB.prepare(
      'SELECT * FROM training_modules WHERE id = ?'
    ).bind(moduleId).first() as any;

    if (!module) {
      return this.jsonResponse({ error: 'Module not found' }, 404);
    }

    const progress = await env.DB.prepare(
      'SELECT * FROM user_training_progress WHERE user_id = ?'
    ).bind(user_id).first() as any;

    const completedModules = progress 
      ? JSON.parse(progress.modules_completed || '[]') 
      : [];

    const prerequisites = JSON.parse(module.prerequisites || '[]');
    if (!this.checkPrerequisites(prerequisites, completedModules)) {
      return this.jsonResponse({
        error: 'Prerequisites not met',
        required: prerequisites,
        completed: completedModules,
      }, 400);
    }

    // Create session
    const sessionId = crypto.randomUUID();
    await env.DB.prepare(`
      INSERT INTO training_sessions (
        id, user_id, module_id, started_at, current_lesson, 
        completed_lessons, score, status
      ) VALUES (?, ?, ?, datetime('now'), 0, '[]', 0, 'in_progress')
    `).bind(sessionId, user_id, moduleId).run();

    const lessons = JSON.parse(module.lessons || '[]');

    return this.jsonResponse({
      session_id: sessionId,
      module: {
        id: module.id,
        title: module.title,
        total_lessons: lessons.length,
      },
      first_lesson: lessons[0] || null,
    });
  },

  // === SIMULATIONS ===
  async listSimulations(url: URL, env: Env): Promise<Response> {
    const deviceType = url.searchParams.get('device_type');
    const difficulty = url.searchParams.get('difficulty');

    let query = 'SELECT * FROM training_simulations WHERE 1=1';
    const params: any[] = [];

    if (deviceType) {
      query += ' AND device_type = ?';
      params.push(deviceType);
    }
    if (difficulty) {
      query += ' AND difficulty = ?';
      params.push(difficulty);
    }

    query += ' ORDER BY difficulty ASC';

    const simulations = await env.DB.prepare(query).bind(...params).all();

    return this.jsonResponse({
      simulations: simulations.results,
      total: simulations.results?.length || 0,
    });
  },

  async startSimulation(simId: string, request: Request, env: Env): Promise<Response> {
    const { user_id } = await request.json() as any;

    const simulation = await env.DB.prepare(
      'SELECT * FROM training_simulations WHERE id = ?'
    ).bind(simId).first() as any;

    if (!simulation) {
      return this.jsonResponse({ error: 'Simulation not found' }, 404);
    }

    // Create simulation session
    const sessionId = crypto.randomUUID();
    const initialState = JSON.parse(simulation.initial_state || '{}');

    await env.DB.prepare(`
      INSERT INTO simulation_sessions (
        id, user_id, simulation_id, started_at, current_state,
        actions_taken, hints_used, mistakes, status
      ) VALUES (?, ?, ?, datetime('now'), ?, '[]', 0, 0, 'in_progress')
    `).bind(
      sessionId, 
      user_id, 
      simId,
      JSON.stringify(initialState)
    ).run();

    return this.jsonResponse({
      session_id: sessionId,
      simulation: {
        id: simulation.id,
        name: simulation.name,
        scenario: simulation.scenario,
        device_type: simulation.device_type,
      },
      initial_state: initialState,
      available_tools: JSON.parse(simulation.available_tools || '[]'),
      available_parts: JSON.parse(simulation.available_parts || '[]'),
      time_limit_seconds: simulation.time_limit_seconds,
      target_symptoms_to_fix: JSON.parse(simulation.target_state || '{}').symptoms || [],
    });
  },

  async performAction(simId: string, request: Request, env: Env): Promise<Response> {
    const { session_id, action } = await request.json() as any;

    const session = await env.DB.prepare(
      'SELECT * FROM simulation_sessions WHERE id = ? AND status = ?'
    ).bind(session_id, 'in_progress').first() as any;

    if (!session) {
      return this.jsonResponse({ error: 'Session not found or completed' }, 404);
    }

    const simulation = await env.DB.prepare(
      'SELECT * FROM training_simulations WHERE id = ?'
    ).bind(simId).first() as any;

    const currentState = JSON.parse(session.current_state);
    const targetState = JSON.parse(simulation.target_state);
    const actions = JSON.parse(session.actions_taken);

    // Process action
    const result = this.processSimulationAction(action, currentState, targetState);
    
    actions.push({
      action,
      timestamp: Date.now(),
      result: result.status,
    });

    // Update session
    let mistakes = session.mistakes;
    if (result.status === 'mistake') {
      mistakes++;
    }

    await env.DB.prepare(`
      UPDATE simulation_sessions SET
        current_state = ?,
        actions_taken = ?,
        mistakes = ?
      WHERE id = ?
    `).bind(
      JSON.stringify(result.newState),
      JSON.stringify(actions),
      mistakes,
      session_id
    ).run();

    // Check if simulation is complete
    const isComplete = this.checkSimulationComplete(result.newState, targetState);

    return this.jsonResponse({
      action_result: result.status,
      feedback: result.feedback,
      new_state: result.newState,
      simulation_complete: isComplete,
      total_actions: actions.length,
      mistakes,
    });
  },

  processSimulationAction(action: any, currentState: DeviceState, targetState: DeviceState): any {
    // Simulate repair action
    const newState = { ...currentState };
    let status = 'success';
    let feedback = '';

    switch (action.type) {
      case 'remove_component':
        if (currentState.components[action.component_id]?.installed) {
          newState.components[action.component_id] = {
            ...newState.components[action.component_id],
            installed: false,
          };
          feedback = `Removed ${action.component_id}`;
        } else {
          status = 'mistake';
          feedback = 'Component is not installed';
        }
        break;

      case 'install_component':
        newState.components[action.component_id] = {
          ...newState.components[action.component_id],
          installed: true,
          condition: 'good',
        };
        feedback = `Installed ${action.component_id}`;
        break;

      case 'connect':
        const connIndex = newState.connections.findIndex(
          c => c.from === action.from && c.to === action.to
        );
        if (connIndex >= 0) {
          newState.connections[connIndex].connected = true;
          feedback = `Connected ${action.from} to ${action.to}`;
        }
        break;

      case 'power_test':
        // Check if all required connections are made
        const allConnected = newState.connections.every(c => c.connected);
        if (allConnected) {
          newState.power_on = true;
          newState.symptoms = newState.symptoms.filter(
            s => !targetState.symptoms?.includes(s)
          );
          feedback = 'Device powered on successfully!';
        } else {
          status = 'mistake';
          feedback = 'Device failed to power on - check connections';
        }
        break;

      default:
        status = 'unknown';
        feedback = 'Unknown action';
    }

    return { status, feedback, newState };
  },

  checkSimulationComplete(currentState: DeviceState, targetState: DeviceState): boolean {
    // Check if current state matches target state
    if (currentState.power_on !== targetState.power_on) return false;
    
    // All symptoms should be fixed
    if (currentState.symptoms.length > 0) return false;
    
    // All target components should be in correct state
    for (const [id, target] of Object.entries(targetState.components)) {
      const current = currentState.components[id];
      if (!current || current.condition !== target.condition) return false;
    }
    
    return true;
  },

  async getHint(simId: string, url: URL, env: Env): Promise<Response> {
    const sessionId = url.searchParams.get('session_id');

    if (!sessionId) {
      return this.jsonResponse({ error: 'Session ID required' }, 400);
    }

    const session = await env.DB.prepare(
      'SELECT * FROM simulation_sessions WHERE id = ?'
    ).bind(sessionId).first() as any;

    if (!session) {
      return this.jsonResponse({ error: 'Session not found' }, 404);
    }

    const simulation = await env.DB.prepare(
      'SELECT hints FROM training_simulations WHERE id = ?'
    ).bind(simId).first() as any;

    const hints = JSON.parse(simulation?.hints || '[]');
    const hintsUsed = session.hints_used;

    if (hintsUsed >= hints.length) {
      return this.jsonResponse({
        hint: 'No more hints available',
        hints_remaining: 0,
      });
    }

    const hint = hints[hintsUsed];

    // Update hints used
    await env.DB.prepare(`
      UPDATE simulation_sessions SET hints_used = hints_used + 1 WHERE id = ?
    `).bind(sessionId).run();

    return this.jsonResponse({
      hint: hint.message,
      penalty_points: hint.penalty_points,
      hints_remaining: hints.length - hintsUsed - 1,
    });
  },

  async completeSimulation(simId: string, request: Request, env: Env): Promise<Response> {
    const { session_id } = await request.json() as any;

    const session = await env.DB.prepare(
      'SELECT * FROM simulation_sessions WHERE id = ?'
    ).bind(session_id).first() as any;

    if (!session) {
      return this.jsonResponse({ error: 'Session not found' }, 404);
    }

    const simulation = await env.DB.prepare(
      'SELECT * FROM training_simulations WHERE id = ?'
    ).bind(simId).first() as any;

    const scoring = JSON.parse(simulation.scoring || '{}');
    const elapsedSeconds = Math.floor(
      (Date.now() - new Date(session.started_at).getTime()) / 1000
    );

    // Calculate score
    let score = 100;
    
    // Time bonus
    if (elapsedSeconds < scoring.time_bonus_threshold) {
      score += scoring.time_bonus_points || 20;
    }
    
    // No hints bonus
    if (session.hints_used === 0) {
      score += scoring.no_hints_bonus || 15;
    }
    
    // Penalty for mistakes
    score -= session.mistakes * (scoring.penalty_per_mistake || 5);
    
    // Penalty for hints
    score -= session.hints_used * 10;
    
    score = Math.max(0, Math.min(score, 100));

    // XP calculation
    const xpEarned = Math.floor(score * 10 * (simulation.difficulty_multiplier || 1));

    // Update session
    await env.DB.prepare(`
      UPDATE simulation_sessions SET 
        status = 'completed',
        score = ?,
        completed_at = datetime('now')
      WHERE id = ?
    `).bind(score, session_id).run();

    // Update user progress
    await this.addXP(session.user_id, xpEarned, env);

    // Check for achievements
    const newAchievements = await this.checkAchievements(session.user_id, {
      simulation_completed: true,
      score,
      no_hints: session.hints_used === 0,
      no_mistakes: session.mistakes === 0,
      time_seconds: elapsedSeconds,
    }, env);

    return this.jsonResponse({
      completed: true,
      score,
      xp_earned: xpEarned,
      time_seconds: elapsedSeconds,
      hints_used: session.hints_used,
      mistakes: session.mistakes,
      new_achievements: newAchievements,
      grade: this.getGrade(score),
    });
  },

  getGrade(score: number): string {
    if (score >= 95) return 'S';
    if (score >= 90) return 'A+';
    if (score >= 85) return 'A';
    if (score >= 80) return 'B+';
    if (score >= 75) return 'B';
    if (score >= 70) return 'C+';
    if (score >= 65) return 'C';
    if (score >= 60) return 'D';
    return 'F';
  },

  // === EXAMS ===
  async startExam(examId: string, request: Request, env: Env): Promise<Response> {
    const { user_id } = await request.json() as any;

    const exam = await env.DB.prepare(
      'SELECT * FROM training_exams WHERE id = ?'
    ).bind(examId).first() as any;

    if (!exam) {
      return this.jsonResponse({ error: 'Exam not found' }, 404);
    }

    const sessionId = crypto.randomUUID();
    const questions = JSON.parse(exam.questions || '[]');
    
    // Randomize question order
    const shuffledQuestions = this.shuffleArray([...questions]);

    await env.DB.prepare(`
      INSERT INTO exam_sessions (
        id, user_id, exam_id, started_at, questions, answers, status
      ) VALUES (?, ?, ?, datetime('now'), ?, '{}', 'in_progress')
    `).bind(
      sessionId,
      user_id,
      examId,
      JSON.stringify(shuffledQuestions.map((q: ExamQuestion) => ({
        id: q.id,
        type: q.type,
        question: q.question,
        options: q.options,
        points: q.points,
      })))
    ).run();

    return this.jsonResponse({
      session_id: sessionId,
      exam: {
        id: exam.id,
        title: exam.title,
        time_limit_minutes: exam.time_limit_minutes,
        passing_score: exam.passing_score,
      },
      questions: shuffledQuestions.map((q: ExamQuestion) => ({
        id: q.id,
        type: q.type,
        question: q.question,
        options: q.options,
        points: q.points,
      })),
      total_questions: shuffledQuestions.length,
    });
  },

  shuffleArray(array: any[]): any[] {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  },

  async submitExam(examId: string, request: Request, env: Env): Promise<Response> {
    const { session_id, answers } = await request.json() as any;

    const session = await env.DB.prepare(
      'SELECT * FROM exam_sessions WHERE id = ? AND status = ?'
    ).bind(session_id, 'in_progress').first() as any;

    if (!session) {
      return this.jsonResponse({ error: 'Session not found or already completed' }, 404);
    }

    const exam = await env.DB.prepare(
      'SELECT * FROM training_exams WHERE id = ?'
    ).bind(examId).first() as any;

    const questions = JSON.parse(exam.questions || '[]');
    
    // Grade exam
    let totalPoints = 0;
    let earnedPoints = 0;
    const results: any[] = [];

    for (const question of questions) {
      totalPoints += question.points;
      const userAnswer = answers[question.id];
      const isCorrect = this.checkAnswer(question, userAnswer);

      if (isCorrect) {
        earnedPoints += question.points;
      }

      results.push({
        question_id: question.id,
        correct: isCorrect,
        user_answer: userAnswer,
        correct_answer: question.correct_answer,
        explanation: question.explanation,
        points_earned: isCorrect ? question.points : 0,
      });
    }

    const score = Math.round((earnedPoints / totalPoints) * 100);
    const passed = score >= exam.passing_score;

    // Update session
    await env.DB.prepare(`
      UPDATE exam_sessions SET 
        status = 'completed',
        answers = ?,
        score = ?,
        passed = ?,
        completed_at = datetime('now')
      WHERE id = ?
    `).bind(
      JSON.stringify(answers),
      score,
      passed ? 1 : 0,
      session_id
    ).run();

    // Award XP and potentially certification
    const xpEarned = passed ? Math.floor(score * 5) : Math.floor(score * 2);
    await this.addXP(session.user_id, xpEarned, env);

    let certification = null;
    if (passed && exam.certification_id) {
      certification = await this.awardCertification(session.user_id, exam.certification_id, env);
    }

    return this.jsonResponse({
      completed: true,
      score,
      passed,
      passing_score: exam.passing_score,
      points_earned: earnedPoints,
      total_points: totalPoints,
      results,
      xp_earned: xpEarned,
      certification,
    });
  },

  checkAnswer(question: ExamQuestion, userAnswer: any): boolean {
    if (Array.isArray(question.correct_answer)) {
      if (Array.isArray(userAnswer)) {
        return JSON.stringify(question.correct_answer.sort()) === 
               JSON.stringify(userAnswer.sort());
      }
      return false;
    }
    return question.correct_answer === userAnswer;
  },

  // === USER PROGRESS ===
  async getProgress(url: URL, env: Env): Promise<Response> {
    const userId = url.searchParams.get('user_id');

    if (!userId) {
      return this.jsonResponse({ error: 'User ID required' }, 400);
    }

    let progress = await env.DB.prepare(
      'SELECT * FROM user_training_progress WHERE user_id = ?'
    ).bind(userId).first() as any;

    if (!progress) {
      // Create new progress record
      await env.DB.prepare(`
        INSERT INTO user_training_progress (
          user_id, total_xp, level, modules_completed, certifications,
          achievements, current_streak, longest_streak, skills
        ) VALUES (?, 0, 1, '[]', '[]', '[]', 0, 0, '{}')
      `).bind(userId).run();

      progress = {
        user_id: userId,
        total_xp: 0,
        level: 1,
        modules_completed: '[]',
        certifications: '[]',
        achievements: '[]',
        current_streak: 0,
        longest_streak: 0,
        skills: '{}',
      };
    }

    const xpForNextLevel = this.getXPForLevel(progress.level + 1);
    const xpProgress = progress.total_xp % 1000;

    return this.jsonResponse({
      user_id: userId,
      total_xp: progress.total_xp,
      level: progress.level,
      level_title: this.getLevelTitle(progress.level),
      xp_to_next_level: xpForNextLevel - progress.total_xp,
      level_progress_percent: Math.round((xpProgress / 1000) * 100),
      modules_completed: JSON.parse(progress.modules_completed || '[]'),
      certifications: JSON.parse(progress.certifications || '[]'),
      achievements: JSON.parse(progress.achievements || '[]'),
      current_streak: progress.current_streak,
      longest_streak: progress.longest_streak,
      skills: JSON.parse(progress.skills || '{}'),
    });
  },

  getXPForLevel(level: number): number {
    return level * 1000;
  },

  getLevelTitle(level: number): string {
    const titles = [
      'Apprentice', 'Novice', 'Technician', 'Skilled Tech', 'Expert',
      'Master', 'Grandmaster', 'Legend', 'Mythic', 'Transcendent'
    ];
    return titles[Math.min(level - 1, titles.length - 1)];
  },

  async addXP(userId: string, xp: number, env: Env): Promise<void> {
    await env.DB.prepare(`
      UPDATE user_training_progress SET 
        total_xp = total_xp + ?,
        level = (total_xp + ?) / 1000 + 1
      WHERE user_id = ?
    `).bind(xp, xp, userId).run();
  },

  async getSkillTree(url: URL, env: Env): Promise<Response> {
    const userId = url.searchParams.get('user_id');

    if (!userId) {
      return this.jsonResponse({ error: 'User ID required' }, 400);
    }

    const progress = await env.DB.prepare(
      'SELECT skills FROM user_training_progress WHERE user_id = ?'
    ).bind(userId).first() as any;

    const skills = JSON.parse(progress?.skills || '{}');

    // Define skill tree structure
    const skillTree = {
      fundamentals: {
        name: 'Fundamentals',
        skills: [
          { id: 'safety', name: 'Safety Protocols', level: skills.safety || 0, maxLevel: 5 },
          { id: 'tools', name: 'Tool Proficiency', level: skills.tools || 0, maxLevel: 5 },
          { id: 'esd', name: 'ESD Handling', level: skills.esd || 0, maxLevel: 3 },
        ],
      },
      diagnostics: {
        name: 'Diagnostics',
        skills: [
          { id: 'visual', name: 'Visual Inspection', level: skills.visual || 0, maxLevel: 5 },
          { id: 'multimeter', name: 'Multimeter Usage', level: skills.multimeter || 0, maxLevel: 5 },
          { id: 'oscilloscope', name: 'Oscilloscope', level: skills.oscilloscope || 0, maxLevel: 5 },
        ],
      },
      soldering: {
        name: 'Soldering',
        skills: [
          { id: 'through_hole', name: 'Through-Hole', level: skills.through_hole || 0, maxLevel: 5 },
          { id: 'smd', name: 'SMD Soldering', level: skills.smd || 0, maxLevel: 5 },
          { id: 'bga', name: 'BGA Rework', level: skills.bga || 0, maxLevel: 5 },
          { id: 'microsoldering', name: 'Microsoldering', level: skills.microsoldering || 0, maxLevel: 5 },
        ],
      },
      devices: {
        name: 'Device Specialization',
        skills: [
          { id: 'phones', name: 'Smartphones', level: skills.phones || 0, maxLevel: 5 },
          { id: 'tablets', name: 'Tablets', level: skills.tablets || 0, maxLevel: 5 },
          { id: 'laptops', name: 'Laptops', level: skills.laptops || 0, maxLevel: 5 },
          { id: 'consoles', name: 'Game Consoles', level: skills.consoles || 0, maxLevel: 5 },
          { id: 'vintage', name: 'Vintage Electronics', level: skills.vintage || 0, maxLevel: 5 },
        ],
      },
    };

    return this.jsonResponse({
      skill_tree: skillTree,
      total_skill_points: Object.values(skills).reduce((a: number, b: any) => a + b, 0),
    });
  },

  // === ACHIEVEMENTS ===
  async getAchievements(url: URL, env: Env): Promise<Response> {
    const userId = url.searchParams.get('user_id');

    // Get all achievements
    const allAchievements = await env.DB.prepare(
      'SELECT * FROM achievements ORDER BY rarity DESC'
    ).all();

    let userAchievements: string[] = [];
    if (userId) {
      const progress = await env.DB.prepare(
        'SELECT achievements FROM user_training_progress WHERE user_id = ?'
      ).bind(userId).first() as any;
      userAchievements = JSON.parse(progress?.achievements || '[]');
    }

    const enriched = (allAchievements.results || []).map((ach: any) => ({
      ...ach,
      condition: JSON.parse(ach.condition || '{}'),
      earned: userAchievements.includes(ach.id),
    }));

    return this.jsonResponse({
      achievements: enriched,
      earned_count: userAchievements.length,
      total_count: enriched.length,
    });
  },

  async checkAchievements(userId: string, context: any, env: Env): Promise<string[]> {
    const progress = await env.DB.prepare(
      'SELECT * FROM user_training_progress WHERE user_id = ?'
    ).bind(userId).first() as any;

    if (!progress) return [];

    const earned = JSON.parse(progress.achievements || '[]');
    const newAchievements: string[] = [];

    // Check for new achievements based on context
    if (context.simulation_completed && context.score === 100 && !earned.includes('perfect_sim')) {
      newAchievements.push('perfect_sim');
    }

    if (context.no_hints && !earned.includes('no_hints_master')) {
      newAchievements.push('no_hints_master');
    }

    if (context.no_mistakes && !earned.includes('flawless')) {
      newAchievements.push('flawless');
    }

    // Update user achievements
    if (newAchievements.length > 0) {
      const updatedAchievements = [...earned, ...newAchievements];
      await env.DB.prepare(`
        UPDATE user_training_progress SET achievements = ? WHERE user_id = ?
      `).bind(JSON.stringify(updatedAchievements), userId).run();
    }

    return newAchievements;
  },

  async claimAchievement(achievementId: string, request: Request, env: Env): Promise<Response> {
    const { user_id } = await request.json() as any;

    const achievement = await env.DB.prepare(
      'SELECT * FROM achievements WHERE id = ?'
    ).bind(achievementId).first() as any;

    if (!achievement) {
      return this.jsonResponse({ error: 'Achievement not found' }, 404);
    }

    // Award XP
    await this.addXP(user_id, achievement.xp_reward, env);

    return this.jsonResponse({
      claimed: true,
      achievement: {
        ...achievement,
        condition: JSON.parse(achievement.condition || '{}'),
      },
      xp_awarded: achievement.xp_reward,
    });
  },

  // === CERTIFICATIONS ===
  async getCertifications(url: URL, env: Env): Promise<Response> {
    const userId = url.searchParams.get('user_id');

    const allCerts = await env.DB.prepare(
      'SELECT * FROM certifications ORDER BY level ASC'
    ).all();

    let userCerts: any[] = [];
    if (userId) {
      const result = await env.DB.prepare(
        'SELECT * FROM user_certifications WHERE user_id = ?'
      ).bind(userId).all();
      userCerts = result.results || [];
    }

    const enriched = (allCerts.results || []).map((cert: any) => {
      const userCert = userCerts.find((uc: any) => uc.certification_id === cert.id);
      return {
        ...cert,
        earned: !!userCert,
        earned_at: userCert?.earned_at,
        expires_at: userCert?.expires_at,
        credential_id: userCert?.credential_id,
      };
    });

    return this.jsonResponse({
      certifications: enriched,
      earned_count: userCerts.length,
    });
  },

  async awardCertification(userId: string, certId: string, env: Env): Promise<any> {
    const certification = await env.DB.prepare(
      'SELECT * FROM certifications WHERE id = ?'
    ).bind(certId).first() as any;

    if (!certification) return null;

    const credentialId = `NL-${Date.now().toString(36).toUpperCase()}-${userId.substring(0, 4).toUpperCase()}`;
    const expiresAt = new Date();
    expiresAt.setMonth(expiresAt.getMonth() + certification.valid_months);

    await env.DB.prepare(`
      INSERT INTO user_certifications (
        id, user_id, certification_id, credential_id, earned_at, expires_at
      ) VALUES (?, ?, ?, ?, datetime('now'), ?)
    `).bind(
      crypto.randomUUID(),
      userId,
      certId,
      credentialId,
      expiresAt.toISOString()
    ).run();

    return {
      certification_id: certId,
      name: certification.name,
      credential_id: credentialId,
      expires_at: expiresAt.toISOString(),
      badge_url: certification.badge_url,
    };
  },

  async verifyCertification(credentialId: string, env: Env): Promise<Response> {
    const cert = await env.DB.prepare(`
      SELECT uc.*, c.name, c.description, u.name as holder_name
      FROM user_certifications uc
      JOIN certifications c ON c.id = uc.certification_id
      JOIN users u ON u.id = uc.user_id
      WHERE uc.credential_id = ?
    `).bind(credentialId).first() as any;

    if (!cert) {
      return this.jsonResponse({ valid: false, error: 'Certification not found' }, 404);
    }

    const isExpired = new Date(cert.expires_at) < new Date();

    return this.jsonResponse({
      valid: !isExpired,
      credential_id: credentialId,
      holder_name: cert.holder_name,
      certification_name: cert.name,
      description: cert.description,
      earned_at: cert.earned_at,
      expires_at: cert.expires_at,
      status: isExpired ? 'EXPIRED' : 'VALID',
    });
  },

  // === LEADERBOARDS ===
  async getLeaderboard(url: URL, env: Env): Promise<Response> {
    const type = url.searchParams.get('type') || 'xp';
    const limit = parseInt(url.searchParams.get('limit') || '50');

    let orderBy = 'total_xp DESC';
    if (type === 'streak') orderBy = 'longest_streak DESC';
    if (type === 'certs') orderBy = '(SELECT COUNT(*) FROM user_certifications WHERE user_id = user_training_progress.user_id) DESC';

    const leaderboard = await env.DB.prepare(`
      SELECT 
        utp.user_id,
        u.name,
        utp.total_xp,
        utp.level,
        utp.current_streak,
        utp.longest_streak,
        (SELECT COUNT(*) FROM user_certifications WHERE user_id = utp.user_id) as certification_count
      FROM user_training_progress utp
      JOIN users u ON u.id = utp.user_id
      ORDER BY ${orderBy}
      LIMIT ?
    `).bind(limit).all();

    const ranked = (leaderboard.results || []).map((entry: any, index) => ({
      rank: index + 1,
      ...entry,
      level_title: this.getLevelTitle(entry.level),
    }));

    return this.jsonResponse({
      type,
      leaderboard: ranked,
    });
  },

  async getWeeklyLeaderboard(env: Env): Promise<Response> {
    // Weekly XP earned
    const weekly = await env.DB.prepare(`
      SELECT 
        user_id,
        SUM(xp_earned) as weekly_xp
      FROM xp_log 
      WHERE created_at > datetime('now', '-7 days')
      GROUP BY user_id
      ORDER BY weekly_xp DESC
      LIMIT 20
    `).all();

    return this.jsonResponse({
      period: 'weekly',
      leaderboard: weekly.results,
    });
  },

  // === CHALLENGES ===
  async getDailyChallenge(env: Env): Promise<Response> {
    const today = new Date().toISOString().split('T')[0];
    
    // Check cache
    const cached = await env.TRAINING_KV.get(`daily_challenge_${today}`);
    if (cached) {
      return this.jsonResponse(JSON.parse(cached));
    }

    // Generate daily challenge
    const simulations = await env.DB.prepare(
      'SELECT id, name, device_type, difficulty FROM training_simulations ORDER BY RANDOM() LIMIT 1'
    ).first() as any;

    const challenge = {
      id: `daily_${today}`,
      date: today,
      type: 'simulation',
      simulation: simulations,
      bonus_xp: 500,
      time_limit_hours: 24,
      requirements: {
        min_score: 80,
        max_hints: 1,
      },
    };

    // Cache for the day
    await env.TRAINING_KV.put(`daily_challenge_${today}`, JSON.stringify(challenge), {
      expirationTtl: 86400,
    });

    return this.jsonResponse(challenge);
  },

  async getWeeklyChallenge(env: Env): Promise<Response> {
    // Get current week number
    const now = new Date();
    const weekNum = Math.ceil((now.getTime() - new Date(now.getFullYear(), 0, 1).getTime()) / 604800000);
    const weekKey = `${now.getFullYear()}_W${weekNum}`;

    const cached = await env.TRAINING_KV.get(`weekly_challenge_${weekKey}`);
    if (cached) {
      return this.jsonResponse(JSON.parse(cached));
    }

    const challenge = {
      id: `weekly_${weekKey}`,
      week: weekKey,
      type: 'multi_simulation',
      simulations: 3,
      bonus_xp: 2000,
      badge_reward: 'weekly_champion',
      requirements: {
        complete_all: true,
        avg_score: 75,
      },
    };

    await env.TRAINING_KV.put(`weekly_challenge_${weekKey}`, JSON.stringify(challenge), {
      expirationTtl: 604800,
    });

    return this.jsonResponse(challenge);
  },

  async submitChallenge(challengeId: string, request: Request, env: Env): Promise<Response> {
    const { user_id, session_ids, scores } = await request.json() as any;

    // Verify challenge completion
    const avgScore = scores.reduce((a: number, b: number) => a + b, 0) / scores.length;
    const passed = avgScore >= 75;

    if (passed) {
      // Award bonus XP
      const bonusXP = challengeId.startsWith('daily') ? 500 : 2000;
      await this.addXP(user_id, bonusXP, env);
    }

    return this.jsonResponse({
      challenge_id: challengeId,
      passed,
      avg_score: avgScore,
      bonus_xp: passed ? (challengeId.startsWith('daily') ? 500 : 2000) : 0,
    });
  },

  // === AI ASSESSMENT ===
  async assessSkill(request: Request, env: Env): Promise<Response> {
    const { user_id, skill_category, test_results } = await request.json() as any;

    // Use AI to assess skill level
    const assessment = await env.AI.run('@cf/meta/llama-3.1-8b-instruct', {
      messages: [{
        role: 'system',
        content: 'You are an expert repair technician trainer assessing student skills.'
      }, {
        role: 'user',
        content: `Assess this student's ${skill_category} skill level based on their performance:
        ${JSON.stringify(test_results)}
        
        Return JSON:
        {
          "skill_level": 1-5,
          "strengths": [],
          "weaknesses": [],
          "recommended_practice": [],
          "confidence": "high|medium|low"
        }`
      }]
    });

    return this.jsonResponse({
      skill_category,
      assessment,
    });
  },

  async identifyWeaknesses(url: URL, env: Env): Promise<Response> {
    const userId = url.searchParams.get('user_id');

    if (!userId) {
      return this.jsonResponse({ error: 'User ID required' }, 400);
    }

    // Analyze user's simulation and exam history
    const simResults = await env.DB.prepare(`
      SELECT 
        ts.device_type,
        AVG(ss.score) as avg_score,
        AVG(ss.mistakes) as avg_mistakes,
        COUNT(*) as attempts
      FROM simulation_sessions ss
      JOIN training_simulations ts ON ts.id = ss.simulation_id
      WHERE ss.user_id = ? AND ss.status = 'completed'
      GROUP BY ts.device_type
    `).bind(userId).all();

    const weakAreas = (simResults.results || [])
      .filter((r: any) => r.avg_score < 70 || r.avg_mistakes > 3)
      .map((r: any) => ({
        area: r.device_type,
        avg_score: Math.round(r.avg_score),
        avg_mistakes: Math.round(r.avg_mistakes * 10) / 10,
        recommendation: `Practice more ${r.device_type} simulations`,
      }));

    return this.jsonResponse({
      weak_areas: weakAreas,
      total_areas_analyzed: simResults.results?.length || 0,
    });
  },

  async getRecommendations(url: URL, env: Env): Promise<Response> {
    const userId = url.searchParams.get('user_id');

    if (!userId) {
      return this.jsonResponse({ error: 'User ID required' }, 400);
    }

    const progress = await env.DB.prepare(
      'SELECT * FROM user_training_progress WHERE user_id = ?'
    ).bind(userId).first() as any;

    const completedModules = JSON.parse(progress?.modules_completed || '[]');
    const skills = JSON.parse(progress?.skills || '{}');

    // Find next recommended modules
    const nextModules = await env.DB.prepare(`
      SELECT * FROM training_modules 
      WHERE id NOT IN (${completedModules.map(() => '?').join(',') || "''"})
      ORDER BY skill_points ASC
      LIMIT 3
    `).bind(...completedModules).all();

    // Find skill gaps
    const skillGaps = Object.entries(skills)
      .filter(([_, level]) => (level as number) < 3)
      .map(([skill, level]) => ({ skill, level, gap: 3 - (level as number) }));

    return this.jsonResponse({
      recommended_modules: nextModules.results,
      skill_gaps: skillGaps,
      daily_challenge_available: true,
      suggested_practice_time: '30 minutes',
    });
  },

  jsonResponse(data: any, status = 200): Response {
    return new Response(JSON.stringify(data), {
      status,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
    });
  },
};
