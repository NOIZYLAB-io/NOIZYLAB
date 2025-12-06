document.getElementById('voiceTrigger').addEventListener('click', () => {
  const status = document.getElementById('status');
  status.textContent = '🎧 Listening for voice command...';

  // Simulate voice onboarding ritual
  setTimeout(() => {
    status.textContent = '✅ Voice ritual complete. IAM badge generated.';
    // Log to console or future audit trail
    console.log(`[${new Date().toISOString()}] Voice onboarding completed.`);
  }, 3000);
});
