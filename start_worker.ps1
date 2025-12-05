# 🧠 RAY WORKER - START ON OMEN
# Fish Music Inc - CB_01

param(
    [string]$GabrielIP = "192.168.1.100"
)

Write-Host ""
Write-Host "🧠 Starting Ray WORKER on OMEN..."
Write-Host "   Connecting to GABRIEL: $GabrielIP"
Write-Host ""

# Stop existing
ray stop 2>$null

# Start worker
ray start `
    --address="$GabrielIP`:6379" `
    --num-cpus=14 `
    --num-gpus=1

Write-Host ""
Write-Host "✅ Ray WORKER connected!"
Write-Host "   Dashboard: http://$GabrielIP`:8265"
Write-Host ""
Write-Host "🔥 GORUNFREE! 🎸🔥"
Write-Host ""
pause
