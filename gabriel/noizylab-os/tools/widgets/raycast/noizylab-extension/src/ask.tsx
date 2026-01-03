import { Detail, LaunchProps, showToast, Toast } from "@raycast/api";
import { useState, useEffect } from "react";

interface AskArguments {
  question: string;
}

export default function Command(props: LaunchProps<{ arguments: AskArguments }>) {
  const { question } = props.arguments;
  const [answer, setAnswer] = useState<string>("Thinking...");
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    async function askAI() {
      try {
        // Route to appropriate worker based on question keywords
        const worker = routeQuestion(question);
        
        showToast({
          style: Toast.Style.Animated,
          title: `Asking ${worker} worker...`,
        });

        // In production, this would call the actual worker
        // For now, simulate a response
        setTimeout(() => {
          setAnswer(getSimulatedResponse(question, worker));
          setIsLoading(false);
          showToast({
            style: Toast.Style.Success,
            title: "Answer received!",
          });
        }, 1500);

      } catch (error) {
        setAnswer("Error querying NoizyLab AI");
        setIsLoading(false);
      }
    }
    askAI();
  }, [question]);

  const markdown = `
# 🧠 NoizyLab AI Response

## Question
> ${question}

## Answer
${answer}

---
*Powered by NoizyLab OS - 57 AI Workers*
  `;

  return <Detail isLoading={isLoading} markdown={markdown} />;
}

function routeQuestion(question: string): string {
  const q = question.toLowerCase();
  if (q.includes("cpu") || q.includes("processor") || q.includes("x86") || q.includes("arm")) return "cpu-architecture";
  if (q.includes("os") || q.includes("operating system") || q.includes("linux") || q.includes("windows")) return "operating-systems";
  if (q.includes("gpu") || q.includes("graphics") || q.includes("cuda") || q.includes("nvidia")) return "gpu-computing";
  if (q.includes("network") || q.includes("tcp") || q.includes("protocol")) return "network-protocols";
  if (q.includes("database") || q.includes("sql") || q.includes("nosql")) return "database-systems";
  if (q.includes("ai") || q.includes("machine learning") || q.includes("neural")) return "ai-ml-history";
  if (q.includes("security") || q.includes("encryption") || q.includes("hack")) return "security-systems";
  if (q.includes("quantum")) return "quantum-computing";
  if (q.includes("compiler") || q.includes("llvm")) return "compiler-technology";
  if (q.includes("docker") || q.includes("vm") || q.includes("kubernetes")) return "virtualization";
  if (q.includes("memory") || q.includes("ram") || q.includes("ddr")) return "memory-systems";
  if (q.includes("storage") || q.includes("ssd") || q.includes("nvme")) return "storage-evolution";
  if (q.includes("display") || q.includes("oled") || q.includes("monitor")) return "display-technology";
  return "brain"; // Default to main AI
}

function getSimulatedResponse(question: string, worker: string): string {
  return `Based on the **${worker}** knowledge base:

This question would be processed by the ${worker} worker, which has comprehensive knowledge about this domain.

**Worker Capabilities:**
- Full historical context
- Technical specifications
- AI-powered analysis
- Real-time data when deployed

*Deploy workers with \`./deploy.sh deploy\` to enable live queries.*`;
}
