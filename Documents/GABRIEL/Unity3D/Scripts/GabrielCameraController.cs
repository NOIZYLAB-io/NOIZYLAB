/*
 * ✨ GABRIEL CAMERA CONTROLLER - CINEMATIC CAMERA SYSTEM ✨
 * 
 * Advanced camera system for GABRIEL with:
 * - Smooth follow
 * - Orbit controls
 * - Cinematic angles
 * - Dynamic zoom
 * - Collision avoidance
 * 
 * Version: 1.0 ULTIMATE
 * Created: November 11, 2025
 */

using UnityEngine;

namespace Gabriel.Ultimate
{
    public class GabrielCameraController : MonoBehaviour
    {
        [Header("Target Settings")]
        [SerializeField] private Transform target;
        [SerializeField] private Vector3 targetOffset = new Vector3(0, 1.5f, 0);

        [Header("Orbit Settings")]
        [SerializeField] private float distance = 5.0f;
        [SerializeField] private float minDistance = 2.0f;
        [SerializeField] private float maxDistance = 10.0f;
        [SerializeField] private float orbitSpeed = 5.0f;
        [SerializeField] private float zoomSpeed = 2.0f;

        [Header("Angle Settings")]
        [SerializeField] private float pitch = 20f;
        [SerializeField] private float minPitch = -10f;
        [SerializeField] private float maxPitch = 60f;
        [SerializeField] private float yaw = 0f;

        [Header("Smooth Settings")]
        [SerializeField] private float positionSmoothing = 5.0f;
        [SerializeField] private float rotationSmoothing = 5.0f;

        [Header("Collision")]
        [SerializeField] private bool avoidCollisions = true;
        [SerializeField] private LayerMask collisionLayers;
        [SerializeField] private float collisionBuffer = 0.2f;

        [Header("Cinematic Presets")]
        [SerializeField] private bool enableCinematicMode = false;
        [SerializeField] private CinematicPreset currentPreset = CinematicPreset.Default;

        public enum CinematicPreset
        {
            Default,
            CloseUp,
            MediumShot,
            WideShot,
            OverShoulder,
            LowAngle,
            HighAngle
        }

        private Camera cam;
        private Vector3 currentVelocity;
        private float currentDistance;
        private bool isOrbiting = false;

        void Awake()
        {
            cam = GetComponent<Camera>();
            currentDistance = distance;
        }

        void LateUpdate()
        {
            if (!target) return;

            HandleInput();
            
            if (enableCinematicMode)
            {
                UpdateCinematicCamera();
            }
            else
            {
                UpdateOrbitCamera();
            }

            if (avoidCollisions)
            {
                HandleCollisions();
            }
        }

        private void HandleInput()
        {
            // Mouse right-click for orbit
            if (Input.GetMouseButton(1))
            {
                isOrbiting = true;
                Cursor.lockState = CursorLockMode.Locked;

                float mouseX = Input.GetAxis("Mouse X");
                float mouseY = Input.GetAxis("Mouse Y");

                yaw += mouseX * orbitSpeed;
                pitch -= mouseY * orbitSpeed;
                pitch = Mathf.Clamp(pitch, minPitch, maxPitch);
            }
            else
            {
                isOrbiting = false;
                Cursor.lockState = CursorLockMode.None;
            }

            // Mouse wheel for zoom
            float scroll = Input.GetAxis("Mouse ScrollWheel");
            if (Mathf.Abs(scroll) > 0.01f)
            {
                currentDistance -= scroll * zoomSpeed;
                currentDistance = Mathf.Clamp(currentDistance, minDistance, maxDistance);
            }

            // Cinematic preset hotkeys
            if (Input.GetKeyDown(KeyCode.C)) CycleCinematicPreset();
            if (Input.GetKeyDown(KeyCode.F1)) SetCinematicPreset(CinematicPreset.CloseUp);
            if (Input.GetKeyDown(KeyCode.F2)) SetCinematicPreset(CinematicPreset.MediumShot);
            if (Input.GetKeyDown(KeyCode.F3)) SetCinematicPreset(CinematicPreset.WideShot);
        }

        private void UpdateOrbitCamera()
        {
            // Calculate target position
            Vector3 targetPoint = target.position + targetOffset;

            // Calculate orbit position
            Quaternion rotation = Quaternion.Euler(pitch, yaw, 0);
            Vector3 offset = rotation * new Vector3(0, 0, -currentDistance);
            Vector3 desiredPosition = targetPoint + offset;

            // Smooth movement
            transform.position = Vector3.SmoothDamp(
                transform.position,
                desiredPosition,
                ref currentVelocity,
                1f / positionSmoothing
            );

            // Look at target
            Quaternion desiredRotation = Quaternion.LookRotation(targetPoint - transform.position);
            transform.rotation = Quaternion.Slerp(
                transform.rotation,
                desiredRotation,
                rotationSmoothing * Time.deltaTime
            );
        }

        private void UpdateCinematicCamera()
        {
            Vector3 targetPoint = target.position + targetOffset;
            Vector3 offset = GetCinematicOffset(currentPreset);

            // Apply preset
            Vector3 desiredPosition = targetPoint + offset;

            // Smooth movement
            transform.position = Vector3.SmoothDamp(
                transform.position,
                desiredPosition,
                ref currentVelocity,
                1f / positionSmoothing
            );

            // Look at target
            Quaternion desiredRotation = Quaternion.LookRotation(targetPoint - transform.position);
            transform.rotation = Quaternion.Slerp(
                transform.rotation,
                desiredRotation,
                rotationSmoothing * Time.deltaTime
            );
        }

        private Vector3 GetCinematicOffset(CinematicPreset preset)
        {
            switch (preset)
            {
                case CinematicPreset.CloseUp:
                    return new Vector3(0, 0.5f, -2f);
                
                case CinematicPreset.MediumShot:
                    return new Vector3(0, 1f, -4f);
                
                case CinematicPreset.WideShot:
                    return new Vector3(0, 2f, -8f);
                
                case CinematicPreset.OverShoulder:
                    return new Vector3(1f, 0.8f, -3f);
                
                case CinematicPreset.LowAngle:
                    return new Vector3(0, -0.5f, -4f);
                
                case CinematicPreset.HighAngle:
                    return new Vector3(0, 3f, -5f);
                
                default:
                    return new Vector3(0, 1.5f, -5f);
            }
        }

        private void HandleCollisions()
        {
            Vector3 targetPoint = target.position + targetOffset;
            Vector3 direction = transform.position - targetPoint;
            float desiredDistance = direction.magnitude;

            RaycastHit hit;
            if (Physics.Raycast(targetPoint, direction.normalized, out hit, desiredDistance, collisionLayers))
            {
                // Move camera in front of collision
                float adjustedDistance = hit.distance - collisionBuffer;
                Vector3 adjustedPosition = targetPoint + direction.normalized * adjustedDistance;
                transform.position = adjustedPosition;
            }
        }

        public void SetTarget(Transform newTarget)
        {
            target = newTarget;
        }

        public void SetCinematicPreset(CinematicPreset preset)
        {
            currentPreset = preset;
            enableCinematicMode = true;
            Debug.Log($"🎬 Camera preset: {preset}");
        }

        public void CycleCinematicPreset()
        {
            int nextIndex = ((int)currentPreset + 1) % System.Enum.GetValues(typeof(CinematicPreset)).Length;
            SetCinematicPreset((CinematicPreset)nextIndex);
        }

        public void EnableFreeCamera()
        {
            enableCinematicMode = false;
        }

        void OnDrawGizmosSelected()
        {
            if (!target) return;

            Vector3 targetPoint = target.position + targetOffset;
            Gizmos.color = Color.cyan;
            Gizmos.DrawWireSphere(targetPoint, 0.3f);
            Gizmos.DrawLine(targetPoint, transform.position);
        }
    }
}
