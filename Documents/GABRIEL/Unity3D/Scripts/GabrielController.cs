/*
 * ✨ GABRIEL ULTIMATE SMOOTH - UNITY 3D CONTROLLER ✨
 * 
 * Main controller for GABRIEL's 3D avatar with smooth movement,
 * animation blending, and intelligent behaviors.
 * 
 * Features:
 * - Smooth character movement with NavMesh
 * - Animation state blending (Idle, Walk, Run, Gesture)
 * - Camera follow system
 * - Input handling (WASD, mouse, voice)
 * - Integration with GABRIEL's AI systems
 * 
 * Version: 1.0 ULTIMATE
 * Created: November 11, 2025
 */

using UnityEngine;
using UnityEngine.AI;
using System.Collections;
using System.Collections.Generic;

namespace Gabriel.Ultimate
{
    [RequireComponent(typeof(NavMeshAgent))]
    [RequireComponent(typeof(Animator))]
    public class GabrielController : MonoBehaviour
    {
        #region Inspector Variables
        [Header("Movement Settings")]
        [SerializeField] private float walkSpeed = 2.0f;
        [SerializeField] private float runSpeed = 5.0f;
        [SerializeField] private float rotationSpeed = 10.0f;
        [SerializeField] private float smoothTime = 0.1f;

        [Header("Animation Settings")]
        [SerializeField] private float animationBlendSpeed = 5.0f;
        [SerializeField] private bool useRootMotion = true;

        [Header("Camera Settings")]
        [SerializeField] private Transform cameraTarget;
        [SerializeField] private Vector3 cameraOffset = new Vector3(0, 2, -5);
        [SerializeField] private float cameraSmooth = 5.0f;

        [Header("Interaction Settings")]
        [SerializeField] private float interactionRange = 3.0f;
        [SerializeField] private LayerMask interactableLayer;

        [Header("AI Integration")]
        [SerializeField] private bool enableProactiveAI = true;
        [SerializeField] private float aiUpdateInterval = 2.0f;
        #endregion

        #region Private Variables
        private NavMeshAgent navAgent;
        private Animator animator;
        private Camera mainCamera;
        
        // Animation parameters
        private int speedParam;
        private int isWalkingParam;
        private int isRunningParam;
        private int gestureParam;
        private int emotionParam;
        
        // Movement state
        private Vector3 moveDirection;
        private float currentSpeed;
        private bool isMoving;
        private bool isRunning;
        
        // Interaction state
        private GameObject currentInteractable;
        private bool isInteracting;
        
        // AI state
        private GabrielAIBridge aiBridge;
        private float lastAIUpdate;
        private string currentEmotion = "calm";
        
        // Smoothing
        private Vector3 velocity;
        private float speedVelocity;
        #endregion

        #region Unity Lifecycle
        void Awake()
        {
            InitializeComponents();
            InitializeAnimationParameters();
            InitializeAI();
        }

        void Start()
        {
            SetupNavMesh();
            SetupCamera();
            
            Debug.Log("🌟 GABRIEL Controller initialized - Ultimate Smooth Mode");
        }

        void Update()
        {
            HandleInput();
            UpdateMovement();
            UpdateAnimation();
            UpdateAI();
            DetectInteractables();
        }

        void LateUpdate()
        {
            UpdateCameraFollow();
        }

        void OnAnimatorMove()
        {
            if (useRootMotion && isMoving)
            {
                navAgent.velocity = animator.deltaPosition / Time.deltaTime;
            }
        }
        #endregion

        #region Initialization
        private void InitializeComponents()
        {
            navAgent = GetComponent<NavMeshAgent>();
            animator = GetComponent<Animator>();
            mainCamera = Camera.main;
            
            if (!mainCamera)
            {
                Debug.LogError("Main camera not found!");
            }
        }

        private void InitializeAnimationParameters()
        {
            speedParam = Animator.StringToHash("Speed");
            isWalkingParam = Animator.StringToHash("IsWalking");
            isRunningParam = Animator.StringToHash("IsRunning");
            gestureParam = Animator.StringToHash("Gesture");
            emotionParam = Animator.StringToHash("Emotion");
        }

        private void InitializeAI()
        {
            aiBridge = gameObject.AddComponent<GabrielAIBridge>();
            if (aiBridge)
            {
                aiBridge.Initialize(this);
                Debug.Log("✨ GABRIEL AI Bridge connected");
            }
        }

        private void SetupNavMesh()
        {
            navAgent.speed = walkSpeed;
            navAgent.angularSpeed = rotationSpeed * 100f;
            navAgent.acceleration = 8f;
            navAgent.stoppingDistance = 0.5f;
            navAgent.updateRotation = false; // Manual rotation for smoother turning
        }

        private void SetupCamera()
        {
            if (!cameraTarget)
            {
                GameObject targetObj = new GameObject("CameraTarget");
                targetObj.transform.SetParent(transform);
                targetObj.transform.localPosition = Vector3.up * 1.5f; // Chest height
                cameraTarget = targetObj.transform;
            }
        }
        #endregion

        #region Input Handling
        private void HandleInput()
        {
            // Keyboard movement (WASD)
            float horizontal = Input.GetAxis("Horizontal");
            float vertical = Input.GetAxis("Vertical");
            
            moveDirection = new Vector3(horizontal, 0, vertical).normalized;
            
            // Run toggle (Left Shift)
            isRunning = Input.GetKey(KeyCode.LeftShift);
            
            // Mouse click movement
            if (Input.GetMouseButtonDown(0))
            {
                HandleMouseClick();
            }
            
            // Gesture triggers
            if (Input.GetKeyDown(KeyCode.G))
            {
                TriggerGesture("wave");
            }
            
            if (Input.GetKeyDown(KeyCode.T))
            {
                TriggerGesture("think");
            }
            
            // Interaction
            if (Input.GetKeyDown(KeyCode.E) && currentInteractable)
            {
                Interact(currentInteractable);
            }
            
            // Emotion control (for testing)
            if (Input.GetKeyDown(KeyCode.Alpha1)) SetEmotion("calm");
            if (Input.GetKeyDown(KeyCode.Alpha2)) SetEmotion("assertive");
            if (Input.GetKeyDown(KeyCode.Alpha3)) SetEmotion("mysterious");
            if (Input.GetKeyDown(KeyCode.Alpha4)) SetEmotion("wise");
        }

        private void HandleMouseClick()
        {
            Ray ray = mainCamera.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            
            if (Physics.Raycast(ray, out hit, 100f))
            {
                MoveToPosition(hit.point);
            }
        }
        #endregion

        #region Movement System
        private void UpdateMovement()
        {
            if (isInteracting) return;
            
            // Calculate target speed
            float targetSpeed = 0f;
            
            if (moveDirection.magnitude > 0.1f)
            {
                targetSpeed = isRunning ? runSpeed : walkSpeed;
                isMoving = true;
                
                // Move character
                MoveCharacter(moveDirection, targetSpeed);
            }
            else if (navAgent.hasPath && navAgent.remainingDistance > navAgent.stoppingDistance)
            {
                targetSpeed = navAgent.speed;
                isMoving = true;
            }
            else
            {
                isMoving = false;
                targetSpeed = 0f;
            }
            
            // Smooth speed transition
            currentSpeed = Mathf.SmoothDamp(currentSpeed, targetSpeed, ref speedVelocity, smoothTime);
        }

        private void MoveCharacter(Vector3 direction, float speed)
        {
            // Convert input to world space relative to camera
            Vector3 cameraForward = mainCamera.transform.forward;
            Vector3 cameraRight = mainCamera.transform.right;
            
            cameraForward.y = 0;
            cameraRight.y = 0;
            
            cameraForward.Normalize();
            cameraRight.Normalize();
            
            Vector3 moveDir = (cameraForward * direction.z + cameraRight * direction.x);
            
            // Move using NavMesh
            if (moveDir.magnitude > 0.1f)
            {
                Vector3 targetPosition = transform.position + moveDir * speed * Time.deltaTime;
                navAgent.SetDestination(targetPosition);
                
                // Smooth rotation
                RotateTowards(moveDir);
            }
        }

        public void MoveToPosition(Vector3 position)
        {
            navAgent.speed = isRunning ? runSpeed : walkSpeed;
            navAgent.SetDestination(position);
            isMoving = true;
        }

        private void RotateTowards(Vector3 direction)
        {
            if (direction.magnitude < 0.1f) return;
            
            Quaternion targetRotation = Quaternion.LookRotation(direction);
            transform.rotation = Quaternion.Slerp(
                transform.rotation, 
                targetRotation, 
                rotationSpeed * Time.deltaTime
            );
        }

        public void StopMovement()
        {
            navAgent.ResetPath();
            moveDirection = Vector3.zero;
            isMoving = false;
        }
        #endregion

        #region Animation System
        private void UpdateAnimation()
        {
            // Calculate normalized speed (0-1 range)
            float normalizedSpeed = currentSpeed / runSpeed;
            
            // Update animator parameters with smooth blending
            animator.SetFloat(speedParam, normalizedSpeed, animationBlendSpeed * Time.deltaTime, Time.deltaTime);
            animator.SetBool(isWalkingParam, isMoving && !isRunning);
            animator.SetBool(isRunningParam, isMoving && isRunning);
            
            // Emotion layer
            UpdateEmotionLayer();
        }

        private void UpdateEmotionLayer()
        {
            // Map emotion to animator parameter
            int emotionIndex = GetEmotionIndex(currentEmotion);
            animator.SetInteger(emotionParam, emotionIndex);
        }

        private int GetEmotionIndex(string emotion)
        {
            switch (emotion.ToLower())
            {
                case "calm": return 0;
                case "assertive": return 1;
                case "mysterious": return 2;
                case "reassuring": return 3;
                case "commanding": return 4;
                case "wise": return 5;
                default: return 0;
            }
        }

        public void TriggerGesture(string gestureName)
        {
            if (isInteracting) return;
            
            StartCoroutine(PlayGesture(gestureName));
        }

        private IEnumerator PlayGesture(string gestureName)
        {
            isInteracting = true;
            
            // Trigger animation
            animator.SetTrigger(gestureParam);
            animator.SetInteger("GestureType", GetGestureIndex(gestureName));
            
            // Wait for gesture to complete
            yield return new WaitForSeconds(2.0f);
            
            isInteracting = false;
        }

        private int GetGestureIndex(string gesture)
        {
            switch (gesture.ToLower())
            {
                case "wave": return 0;
                case "think": return 1;
                case "nod": return 2;
                case "point": return 3;
                case "confident": return 4;
                default: return 0;
            }
        }

        public void SetEmotion(string emotion)
        {
            currentEmotion = emotion;
            Debug.Log($"🎭 GABRIEL emotion: {emotion}");
            
            // Notify AI bridge
            if (aiBridge)
            {
                aiBridge.OnEmotionChanged(emotion);
            }
        }
        #endregion

        #region Camera System
        private void UpdateCameraFollow()
        {
            if (!mainCamera || !cameraTarget) return;
            
            // Calculate target position
            Vector3 targetPosition = cameraTarget.position + 
                cameraTarget.TransformDirection(cameraOffset);
            
            // Smooth camera movement
            mainCamera.transform.position = Vector3.Lerp(
                mainCamera.transform.position,
                targetPosition,
                cameraSmooth * Time.deltaTime
            );
            
            // Look at target
            mainCamera.transform.LookAt(cameraTarget);
        }
        #endregion

        #region Interaction System
        private void DetectInteractables()
        {
            Collider[] colliders = Physics.OverlapSphere(
                transform.position, 
                interactionRange, 
                interactableLayer
            );
            
            GameObject closest = null;
            float closestDistance = float.MaxValue;
            
            foreach (Collider col in colliders)
            {
                float distance = Vector3.Distance(transform.position, col.transform.position);
                if (distance < closestDistance)
                {
                    closestDistance = distance;
                    closest = col.gameObject;
                }
            }
            
            if (closest != currentInteractable)
            {
                currentInteractable = closest;
                OnInteractableChanged(closest);
            }
        }

        private void OnInteractableChanged(GameObject interactable)
        {
            if (interactable)
            {
                Debug.Log($"💡 Interactable detected: {interactable.name}");
                // Show UI prompt
            }
            else
            {
                // Hide UI prompt
            }
        }

        public void Interact(GameObject target)
        {
            if (!target) return;
            
            StartCoroutine(PerformInteraction(target));
        }

        private IEnumerator PerformInteraction(GameObject target)
        {
            isInteracting = true;
            
            // Stop movement
            StopMovement();
            
            // Face target
            Vector3 direction = (target.transform.position - transform.position).normalized;
            direction.y = 0;
            RotateTowards(direction);
            
            yield return new WaitForSeconds(0.5f);
            
            // Trigger interaction gesture
            TriggerGesture("wave");
            
            // Get AI response
            if (aiBridge)
            {
                string context = $"interacting with {target.name}";
                aiBridge.RequestAIResponse(context);
            }
            
            Debug.Log($"🤝 GABRIEL interacting with: {target.name}");
            
            yield return new WaitForSeconds(2.0f);
            
            isInteracting = false;
        }
        #endregion

        #region AI Integration
        private void UpdateAI()
        {
            if (!enableProactiveAI || !aiBridge) return;
            
            if (Time.time - lastAIUpdate >= aiUpdateInterval)
            {
                lastAIUpdate = Time.time;
                
                // Send context to AI system
                Dictionary<string, object> context = new Dictionary<string, object>
                {
                    { "position", transform.position },
                    { "is_moving", isMoving },
                    { "current_speed", currentSpeed },
                    { "emotion", currentEmotion },
                    { "timestamp", System.DateTime.Now }
                };
                
                aiBridge.UpdateContext(context);
            }
        }

        public void OnAIResponse(string response, string emotion, List<string> suggestions)
        {
            Debug.Log($"🎤 GABRIEL: {response}");
            
            // Update emotion based on AI
            if (!string.IsNullOrEmpty(emotion))
            {
                SetEmotion(emotion);
            }
            
            // Handle proactive suggestions
            if (suggestions != null && suggestions.Count > 0)
            {
                Debug.Log($"💡 Suggestions: {string.Join(", ", suggestions)}");
            }
        }
        #endregion

        #region Public API
        public float GetSpeed() => currentSpeed;
        public bool IsMoving() => isMoving;
        public bool IsRunning() => isRunning;
        public string GetCurrentEmotion() => currentEmotion;
        public Vector3 GetPosition() => transform.position;
        public Quaternion GetRotation() => transform.rotation;
        #endregion

        #region Debug
        void OnDrawGizmosSelected()
        {
            // Interaction range
            Gizmos.color = Color.yellow;
            Gizmos.DrawWireSphere(transform.position, interactionRange);
            
            // Movement direction
            if (moveDirection.magnitude > 0.1f)
            {
                Gizmos.color = Color.green;
                Gizmos.DrawRay(transform.position, moveDirection * 2f);
            }
            
            // NavMesh path
            if (navAgent && navAgent.hasPath)
            {
                Gizmos.color = Color.blue;
                Vector3[] path = navAgent.path.corners;
                for (int i = 0; i < path.Length - 1; i++)
                {
                    Gizmos.DrawLine(path[i], path[i + 1]);
                }
            }
        }
        #endregion
    }
}
