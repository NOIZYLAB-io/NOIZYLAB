import fs from 'fs';
import yaml from 'js-yaml';

const identityPath = '../rituals/identity.yaml';
const logPath = '../logs/init.log';

function generateBadge() {
  try {
    const file = fs.readFileSync(identityPath, 'utf8');
    const data = yaml.load(file);

    const badge = `
      🛡️ IAM Badge
      ───────────────
      Author: ${data.identity.author}
      Brand: ${data.identity.brand}
      Roles:
        ${data.identity.IAM_roles.join('\n        ')}
      Constellation:
        ${data.identity.constellation}
    `;

    console.log(badge);

    fs.appendFileSync(logPath, `[${new Date().toISOString()}] Badge generated for ${data.identity.author}\n`);
  } catch (err) {
    console.error('⚠️ Badge generation failed:', err.message);
  }
}

generateBadge();
