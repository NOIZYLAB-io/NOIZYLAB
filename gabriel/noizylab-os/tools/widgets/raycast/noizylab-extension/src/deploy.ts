import { showHUD, showToast, Toast } from "@raycast/api";
import { exec } from "child_process";
import { promisify } from "util";

const execAsync = promisify(exec);

export default async function Command() {
    try {
        await showToast({
            style: Toast.Style.Animated,
            title: "🚀 Deploying NoizyLab OS...",
            message: "57 workers to Cloudflare",
        });

        // Start deployment in background
        const deployPath = "/Users/m2ultra/NOIZYLAB/GABRIEL/noizylab-os";

        exec(`cd ${deployPath} && ./deploy.sh deploy 2>&1 | tee /tmp/noizylab-deploy.log`, (error) => {
            if (error) {
                showToast({
                    style: Toast.Style.Failure,
                    title: "Deployment failed",
                    message: error.message,
                });
            }
        });

        await showHUD("🚀 NoizyLab OS deployment started! Check /tmp/noizylab-deploy.log for progress");

    } catch (error) {
        await showToast({
            style: Toast.Style.Failure,
            title: "Failed to start deployment",
            message: String(error),
        });
    }
}
