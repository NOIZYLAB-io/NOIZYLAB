#!/usr/bin/env python3
from flask import Flask, render_template, request, send_file
import plistlib
import io
import OpenAI from "openai";


app = Flask(__name__)
client = new OpenAI()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        full_name = request.form.get('full_name', 'User')
        imap_server = request.form['imap_server']
        smtp_server = request.form['smtp_server']
        imap_port = int(request.form.get('imap_port', 993))
        smtp_port = int(request.form.get('smtp_port', 465))

        payload = {
            'PayloadContent': [{
                'EmailAddress': email,
                'IncomingMailServerHostName': imap_server,
                'IncomingMailServerPortNumber': imap_port,
                'IncomingMailServerUseSSL': True,
                'IncomingMailServerUsername': email,
                'OutgoingMailServerHostName': smtp_server,
                'OutgoingMailServerPortNumber': smtp_port,
                'OutgoingMailServerUseSSL': True,
                'OutgoingMailServerUsername': email,
                'OutgoingMailServerAuthentication': True,
                'EmailAccountDescription': f"{email} (Webador)",
                'EmailAccountName': full_name,
                'EmailAccountType': 'EmailTypeIMAP',
                'PayloadType': 'com.apple.mail.managed',
                'PayloadVersion': 1,
                'PayloadIdentifier': f"com.example.{email}.mail",
                'PayloadUUID': email,
                'PayloadDisplayName': f"{email} Email",
            }],
            'PayloadType': 'Configuration',
            'PayloadVersion': 1,
            'PayloadIdentifier': f"com.example.{email}.config",
            'PayloadUUID': email,
            'PayloadDisplayName': f"{email} Config",
        }
        buf = io.BytesIO()
        plistlib.dump(payload, buf)
        buf.seek(0)
        filename = f"{email.replace('@', '_at_')}.mobileconfig"
        return send_file(
            buf,
            as_attachment=True,
            download_name=filename,
            mimetype='application/x-apple-aspen-config'
        )
    return render_template('index.html')


async function main() {
  const response = await client.responses.create({
    model: "gpt-5",
    input: "Write a short bedtime story about a unicorn.",
  });

  console.log(response.output_text);
}

main();


if __name__ == '__main__':
    app.run(debug=True)
