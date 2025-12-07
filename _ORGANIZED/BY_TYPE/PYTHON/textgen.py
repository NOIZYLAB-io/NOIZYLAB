"""NoizySynth Text Generator"""
def generate_text(prompt, context):
    mode = context.get("type", "summary")
    if mode == "report":
        return f"# Repair Report\n\n## Summary\n{prompt}\n\n## Details\nGenerated report content."
    if mode == "session":
        return f"## Session Summary\n\nClient session: {prompt}\n\nStatus: Complete"
    if mode == "diagnostic":
        return f"## Diagnostic Report\n\n{prompt}\n\nAll systems nominal."
    return f"Generated: {prompt}"

