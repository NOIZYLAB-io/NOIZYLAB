import click
from accounts.manager import AccountManager
from twofa.handler import TwoFAHandler
from audio.library import AudioLibrary

@click.group()
def cli():
    """Noizy Fish Orchestrator CLI"""
    pass

@cli.command()
def manage_accounts():
    """Manage accounts and their configurations."""
    manager = AccountManager()
    manager.load_accounts()
    click.echo("Accounts loaded successfully.")
    # Additional account management logic can be added here

@cli.command()
def handle_twofa():
    """Handle two-factor authentication for accounts."""
    twofa_handler = TwoFAHandler()
    twofa_handler.check_twofa_status()
    click.echo("2FA status checked successfully.")
    # Additional 2FA handling logic can be added here

@cli.command()
def scan_audio():
    """Scan audio files and manage the audio library."""
    audio_library = AudioLibrary()
    audio_library.scan_for_audio_files()
    click.echo("Audio files scanned successfully.")
    # Additional audio management logic can be added here

if __name__ == "__main__":
    cli()