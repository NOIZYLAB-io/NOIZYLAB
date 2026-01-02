#!/usr/bin/env python3
"""
VS Code Accessibility + Voice-First Treats
Author: R.S Plowman (Fish Music Inc.)
Purpose: One-stop reference of 100 accessibility, voice, and AI creative features
"""

vs_code_accessibility_100 = """
1. VS Code Speech extension
2. Voice: Start Dictation in Editor
3. Voice: Stop Dictation in Editor
4. Walky-Talky mode
5. Voice in Chat
6. Chat: Start Voice Chat
7. Inline Voice Chat
8. Quick Voice Chat
9. Voice Chat in Chat View
10. "Hey Code" keyword activation
11. Auto-speak responses
12. Selective read-aloud
13. Speech timeout control
14. Voice dictation in commit messages
15. Voice dictation in PR comments
16. Voice dictation in notebooks
17. Voice dictation in terminal
18. Voice dictation in settings search
19. Voice dictation in extensions search
20. Voice dictation in file explorer rename
21. Accessibility Help menu
22. High Contrast themes
23. Color vision accessible themes
24. Custom warning/error colors
25. Zoom in/out/reset
26. Persisted zoom level
27. Screen reader optimized UI
28. Keyboard-only navigation
29. Accessible breadcrumbs
30. Accessible inline chat
31. Custom keybindings
32. Sticky keys (OS-level)
33. On-screen keyboard (OS-level)
34. Voice-to-key mapping (Dragon, Talon)
35. Macros extension
36. Multi-command extension
37. Keyboard Shortcuts Quick Reference
38. Command Palette voice trigger
39. Quick Open voice trigger
40. Task Runner voice trigger
41. Talon Voice integration
42. Cursorless extension
43. Serenade AI
44. Dictation Box extension
45. Speech Notes integration
46. CodeSnap extension
47. Bookmarks extension
48. Project Manager extension
49. Error Lens extension
50. Code Spell Checker
51. Copilot Voice Chat
52. Copilot inline voice prompts
53. Copilot text-to-speech
54. AI image generation extensions
55. AI audio generation extensions
56. AI video scripting extensions
57. Markdown Preview Enhanced
58. Mermaid diagrams by dictation
59. PlantUML diagrams by dictation
60. LaTeX Workshop voice dictation
61. Tasks.json voice triggers
62. Launch.json voice triggers
63. Snippets triggered by voice
64. Code Runner voice execution
65. REST Client voice execution
66. Docker build/run by voice
67. Makefile tasks by voice
68. FFmpeg tasks by voice
69. Git commit/push by voice
70. GitLens blame by voice
71. Remote SSH voice connect
72. Remote Containers voice open
73. WSL voice open
74. Codespaces voice open
75. Dev Tunnels voice open
76. Azure Functions deploy by voice
77. AWS Lambda deploy by voice
78. Firebase deploy by voice
79. Kubernetes apply by voice
80. Docker Compose up by voice
81. Zen Mode voice toggle
82. Focus Mode voice toggle
83. Minimap voice toggle
84. Sidebar voice toggle
85. Panel voice toggle
86. Terminal voice toggle
87. Breadcrumbs voice toggle
88. Outline voice toggle
89. Error Lens voice toggle
90. Spell Checker voice toggle
91. Hey Code always-listening mode
92. Voice-driven refactoring
93. Voice-driven test running
94. Voice-driven debugging
95. Voice-driven breakpoints
96. Voice-driven variable inspection
97. Voice-driven Copilot prompts
98. Voice-driven creative brainstorming
99. Voice-driven diagram generation
100. Voice-driven multi-modal AI (text+audio+visual)
"""

def print_all():
    print(vs_code_accessibility_100)

def search(keyword: str):
    """Search the list for a keyword (case-insensitive)."""
    results = [line for line in vs_code_accessibility_100.splitlines() if keyword.lower() in line.lower()]
    if results:
        print("\n".join(results))
    else:
        print(f"No matches found for '{keyword}'.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="VS Code Accessibility + Voice Treats Reference")
    parser.add_argument("--search", "-s", help="Search for a keyword")
    args = parser.parse_args()

    if args.search:
        search(args.search)
    else:
        print_all()