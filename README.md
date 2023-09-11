# GPT-Dungeon-Master

<div align="center">

![GPT-dungeon-master Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/SverreNystad/gpt-dungeon-master/build_test_pipeline.yml)
[![codecov.io](https://codecov.io/github/SverreNystad/gpt-dungeon-master/coverage.svg?branch=main)]
(https://codecov.io/github/SverreNystad/gpt-dungeon-master?branch=main)
![GPT-dungeon-master top language](https://img.shields.io/github/languages/top/SverreNystad/gpt-dungeon-master)
![GitHub language count](https://img.shields.io/github/languages/count/SverreNystad/gpt-dungeon-master)
[![Project Version](https://img.shields.io/badge/version-0.0.3-blue)](https://img.shields.io/badge/version-0.0.1-blue)

![Alt text](docs/images/DALL·E%202023-09-09%2023.10.21%20-%20A%20robot%20in%20a%20medieval%20cloak%20sitting%20at%20the%20head%20of%20a%20stone%20table,%20with%20AI-driven%20holographic%20projections%20of%20a%2020%20sided%20dice,%20digital%20art.png)


</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary> <b> Table of Contents </b> </summary>
  <ol>
    <li>
    <a href="#GPT-Dungeon-Master"> GPT-Dungeon-Master </a>
    </li>
    <li>
      <a href="#Introduction">Introduction</a>
    </li>
    <li>
      <a href="#Planed-Features">Planed Features</a>
    </li>
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#Installation">Installation</a>
      <ul>
        <li><a href="#Prerequisites">Prerequisites</a></li>
        <li><a href="#Setup">Setup</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## Introduction
Welcome to the GPT Dungeon Master repository! This project harnesses the power of GPT models to create a dynamic and responsive Dungeon Master (DM) for tabletop role-playing games (RPGs). Whether you're a seasoned player looking for a quick rule reference or a group in need of an AI-driven DM for your next adventure, the GPT Dungeon Master is here to guide you.

### Planned Features
**Knowledgebase Integration:** Access a vast digital library of RPG rulebooks. Get instant answers to rule queries, character abilities, and more.

**Dynamic Storytelling:** Let the GPT model craft intricate narratives, describe vivid settings, and generate unexpected plot twists.

**Character Interaction:** Interact with the GPT DM through your character. Ask questions, make requests, and engage in dialogue.

**Text-to-Speech:** Listen to the GPT DM through a text-to-speech engine. Hear the DM's narration, character voices, and more. The voices will be different based on the character.

**Speech-to-Text:** Speak to the GPT DM through a speech-to-text engine. Ask questions, make requests, and engage in dialogue.

**Generative Art:** Experience the GPT DM's imagination through generative art. See the DM's descriptions come to life in real-time.

**Rule Enforcement:** Ensure your gameplay adheres to the rules. The system checks player actions against the rulebook, ensuring a fair and consistent gaming experience.

**Interactive UI:** Engage with the GPT DM through a user-friendly interface. Input actions, ask questions, and immerse yourself in the game.

## Usage
The GPT Dungeon Master is currently in development. Check back later for updates.
```bash
python main.py
```

## Installation
To install the GPT Dungeon Master, one needs to have all the prerequisites installed and set up, and follow the setup guild. The following sections will guide you through the process.
### Prerequisites
- Python 3.6 or higher
- OpenAI API key (https://platform.openai.com/account/api-keys)
  

### Setup
1. Clone the repository
```bash
git clone https://github.com/SverreNystad/gpt-dungeon-master.git
cd gpt-dungeon-master
```
2. Create a virtual environment
    
    #### On Windows:
    ```bash
    python3 -m venv venv
    source venv/Scripts/activate
    ```
    #### On macOS and Linux: 
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages
```bash
pip install -r requirements.txt
```

4. Create a file called `.env` in the root directory of the project. Add the following lines to the file:
```bash
touch .env
echo "OPENAI_API_KEY=YOUR_API_KEY" > .env # Remember to change YOUR_API_KEY to your actual API key
```

### License
The license is not yet decided. Check back later for updates.


### Roadmap (work in progress)
#### Phase 1 Preliminary Setup
Create a repository structure, and set up initial project documentation, survey the best tools for text-to-speech, speech-to-text, the GPT model and generative art.

#### Phase 2 Create tools
Implement most of the planned features, creating a TTS and creating a generative image module, create a text generation module.

#### Phase 3 Core Functionality and polishing
Create the core out of combate functionality like Character interaction and dynamic storytelling. Integrate the different modules.


#### Phase 4 Interactive UI
Creating a user friendly UI to make the project easier to use without deep knolegde of the project. Work on QOL tools like SST engines module or similar tools.

#### Phase 5 Official Release and Future Work
* Launch the official version of the GPT Dungeon Master. 
* Explore the possibility of introducing combat aspects and other advanced features into the system.
