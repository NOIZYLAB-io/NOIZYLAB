import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "YOUR_API_KEY" // Replace with your actual API key
});

async function testOpenAI() {
  try {
    const response = await client.chat.completions.create({
      model: "gpt-4o",
      messages: [
        { role: "user", content: "Say hello!" }
      ]
    });
    console.log("OpenAI API test successful:", response.choices[0].message.content);
  } catch (error) {
    console.error("OpenAI API test failed:", error);
  }
}

testOpenAI();
