# Clone Serenade repository
git clone https://github.com/serenadeai/serenade.git ~/serenade

# Install Serenade (macOS)
cd ~/serenade
./install.sh

# Optionally, install the Serenade VS Code extension
code --install-extension serenade.serenade

echo "Serenade voice coding is installed! Launch Serenade from ~/serenade or use the VS Code extension."

# NoizyFish directory structure
mkdir -p ~/NoizyFish/{instruments/{synths,samplers,drum-machines,effects},plugins/{vst,au,lv2,custom},presets/{synths,samplers,effects},samples/{drums,loops,one-shots},docs,scripts}

# Create README.md in docs directory
touch ~/NoizyFish/docs/README.md

# NoizyFish directory structure
NoizyFish/
├── instruments/
│   ├── synths/
│   ├── samplers/
│   ├── drum-machines/
│   └── effects/
├── plugins/
│   ├── vst/
│   ├── au/
│   ├── lv2/
│   └── custom/
├── presets/
│   ├── synths/
│   ├── samplers/
│   └── effects/
├── samples/
│   ├── drums/
│   ├── loops/
│   └── one-shots/
├── docs/
│   └── README.md
└── scripts/