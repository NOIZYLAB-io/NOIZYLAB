#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
import plistlib
import uuid

#!/usr/bin/env python3
"""
iOS Email Configuration Profile Generator
Creates .mobileconfig files for automatic iOS email setup
"""


class IOSEmailProfileGenerator:
    """Generate iOS email configuration profiles"""

    def __init__(self):
        self.output_dir = Path.home() / ".it_genius" / "ios_profiles"
        self.output_dir.mkdir(exist_ok=True, parents=True)

    def create_email_profile(self, email, display_name, server_settings):
        """Create a single email profile"""
        profile_uuid = str(uuid.uuid4())

        profile = {
            'PayloadContent': [{
                'EmailAccountDescription': display_name,
                'EmailAccountName': email,
                'EmailAccountType': 'EmailTypeIMAP',
                'EmailAddress': email,
                'IncomingMailServerAuthentication': 'EmailAuthPassword',
                'IncomingMailServerHostName': server_settings['imap_server'],
                'IncomingMailServerPortNumber': server_settings['imap_port'],
                'IncomingMailServerUseSSL': True,
                'IncomingMailServerUsername': email,
                'IncomingPassword': '',  # User will enter
                'OutgoingMailServerAuthentication': 'EmailAuthPassword',
                'OutgoingMailServerHostName': server_settings['smtp_server'],
                'OutgoingMailServerPortNumber': server_settings['smtp_port'],
                'OutgoingMailServerUseSSL': True,
                'OutgoingMailServerUsername': email,
                'OutgoingPassword': '',  # User will enter
                'PayloadDescription': f'Email account configuration for {email}',
                'PayloadDisplayName': display_name,
                'PayloadIdentifier': f'com.itgenius.email.{email.replace("@", ".").replace(".", "-")}',
                'PayloadType': 'com.apple.mail.managed',
                'PayloadUUID': str(uuid.uuid4()),
                'PayloadVersion': 1
            }],
            'PayloadDescription': f'Email configuration for {email}',
            'PayloadDisplayName': f'Email: {email}',
            'PayloadIdentifier': f'com.itgenius.profile.{profile_uuid}',
            'PayloadOrganization': 'IT Genius',
            'PayloadRemovalDisallowed': False,
            'PayloadType': 'Configuration',
            'PayloadUUID': profile_uuid,
            'PayloadVersion': 1
        }

        return profile

    def create_all_profiles(self):
        """Create profiles for all email accounts"""
        accounts = {
            'rp@fishmusicinc.com': {
                'display_name': 'Fish Music Inc - RP',
                'server_settings': {
                    'imap_server': 'mail.fishmusicinc.com',
                    'imap_port': 993,
                    'smtp_server': 'mail.fishmusicinc.com',
                    'smtp_port': 587
                }
            },
            'info@fishmusicinc.com': {
                'display_name': 'Fish Music Inc - Info',
                'server_settings': {
                    'imap_server': 'mail.fishmusicinc.com',
                    'imap_port': 993,
                    'smtp_server': 'mail.fishmusicinc.com',
                    'smtp_port': 587
                }
            },
            'rsp@noizylab.ca': {
                'display_name': 'NoizyLab - RSP',
                'server_settings': {
                    'imap_server': 'mail.noizylab.ca',
                    'imap_port': 993,
                    'smtp_server': 'mail.noizylab.ca',
                    'smtp_port': 587
                }
            },
            'help@noizylab.ca': {
                'display_name': 'NoizyLab - Help',
                'server_settings': {
                    'imap_server': 'mail.noizylab.ca',
                    'imap_port': 993,
                    'smtp_server': 'mail.noizylab.ca',
                    'smtp_port': 587
                }
            },
            'hello@noizylab.ca': {
                'display_name': 'NoizyLab - Hello',
                'server_settings': {
                    'imap_server': 'mail.noizylab.ca',
                    'imap_port': 993,
                    'smtp_server': 'mail.noizylab.ca',
                    'smtp_port': 587
                }
            },
            'rsplowman@icloud.com': {
                'display_name': 'iCloud Email',
                'server_settings': {
                    'imap_server': 'imap.mail.me.com',
                    'imap_port': 993,
                    'smtp_server': 'smtp.mail.me.com',
                    'smtp_port': 587
                }
            }
        }

        profiles = []
        for email, config in accounts.items():
            profile = self.create_email_profile(
                email,
                config['display_name'],
                config['server_settings']
            )
            profiles.append((email, profile))

        return profiles

    def save_profile(self, email, profile):
        """Save profile as .mobileconfig file"""
        filename = f"email_{email.replace('@', '_').replace('.', '_')}.mobileconfig"
        filepath = self.output_dir / filename

        with open(filepath, 'wb') as f:
            plistlib.dump(profile, f)

        return filepath

    def create_combined_profile(self, profiles):
        """Create one combined profile with all accounts"""
        combined_uuid = str(uuid.uuid4())

        payload_content = []
        for email, profile in profiles:
            payload_content.append(profile['PayloadContent'][0])

        combined_profile = {
            'PayloadContent': payload_content,
            'PayloadDescription': 'All email accounts configuration',
            'PayloadDisplayName': 'Email Accounts - All',
            'PayloadIdentifier': f'com.itgenius.email.all',
            'PayloadOrganization': 'IT Genius',
            'PayloadRemovalDisallowed': False,
            'PayloadType': 'Configuration',
            'PayloadUUID': combined_uuid,
            'PayloadVersion': 1
        }

        return combined_profile

    def generate_all(self):
        """Generate all profiles"""
        print("\n" + "="*80)
        print("📱 iOS EMAIL CONFIGURATION PROFILE GENERATOR")
        print("="*80)

        profiles = self.create_all_profiles()

        print(f"\n✅ Generated {len(profiles)} email profiles")

        # Save individual profiles
        saved_files = []
        for email, profile in profiles:
            filepath = self.save_profile(email, profile)
            saved_files.append(filepath)
            print(f"  ✅ {email} → {filepath.name}")

        # Create combined profile
        combined = self.create_combined_profile(profiles)
        combined_path = self.output_dir / "all_email_accounts.mobileconfig"
        with open(combined_path, 'wb') as f:
            plistlib.dump(combined, f)
        saved_files.append(combined_path)

        print(f"\n✅ Combined profile: {combined_path.name}")

        print(f"\n📁 Profiles saved to: {self.output_dir}")
        print("\n📱 TO INSTALL ON iOS:")
        print("  1. Transfer .mobileconfig files to iOS device")
        print("  2. Open file on iOS device")
        print("  3. Go to Settings → Profile Downloaded")
        print("  4. Install profile")
        print("  5. Enter passwords when prompted")

        return saved_files

if __name__ == "__main__":
    try:
        generator = IOSEmailProfileGenerator()
            generator.generate_all()


    except Exception as e:
        print(f"Error: {e}")
