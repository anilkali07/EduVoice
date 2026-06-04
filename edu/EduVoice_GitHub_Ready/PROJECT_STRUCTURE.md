# 📋 Project File Structure

```
project Cop/
│
├── 📄 package.json                 # Dependencies and scripts
├── 📄 vite.config.js              # Vite configuration
├── 📄 tailwind.config.js          # Tailwind theme and colors
├── 📄 postcss.config.js           # PostCSS configuration
├── 📄 .eslintrc.cjs               # ESLint rules
├── 📄 .gitignore                  # Git ignore patterns
├── 📄 index.html                  # HTML entry point
│
├── 📁 src/                        # Source code
│   ├── 📄 main.jsx               # React entry point
│   ├── 📄 App.jsx                # Main app component with routing
│   ├── 📄 index.css              # Global styles with Tailwind
│   │
│   ├── 📁 components/            # Reusable components
│   │   ├── Navigation.jsx        # Top navigation bar
│   │   ├── AssistPopover.jsx     # Help popover with simplification
│   │   └── MicrophoneStatus.jsx  # Live mic status indicator
│   │
│   ├── 📁 contexts/              # React contexts
│   │   └── AuthContext.jsx       # Authentication & user state
│   │
│   ├── 📁 pages/                 # Page components
│   │   ├── Login.jsx             # Account selection & login
│   │   ├── Dashboard.jsx         # Main user dashboard
│   │   ├── Reader.jsx            # ⭐ Core reading interface
│   │   ├── Reports.jsx           # Detailed session reports
│   │   └── ParentDashboard.jsx   # Parent view of children
│   │
│   └── 📁 services/              # Service modules
│       ├── ASRService.js         # 🎤 Speech recognition
│       ├── SimplificationService.js # 💡 Text simplification
│       └── TTSService.js         # 🔊 Text-to-speech
│
├── 📁 mockups/                   # UI mockup HTML files
│   ├── mockup-1-reader-listening.html
│   ├── mockup-2-assist-popover.html
│   ├── mockup-3-self-dashboard.html
│   └── mockup-4-parent-dashboard.html
│
├── 📄 README.md                  # Comprehensive documentation
├── 📄 QUICKSTART.md              # Quick setup guide
├── 📄 DESIGN_MOCKUPS.md          # UI design specifications
└── 📄 PROJECT_STRUCTURE.md       # This file
```

---

## 🗂️ Detailed Component Breakdown

### Core Application Files

**`src/App.jsx`**
- Main application component
- React Router setup with protected routes
- Auth-based navigation logic

**`src/main.jsx`**
- React application entry point
- Renders root component

**`src/index.css`**
- Tailwind CSS imports
- Custom CSS for dyslexia-friendly styling
- Animation keyframes

---

### Components (`src/components/`)

**`Navigation.jsx`**
- Top navigation bar
- Responsive mobile menu
- User info display
- Logout functionality

**`AssistPopover.jsx`**
- Modal popup for reading assistance
- Displays simplified word, explanation, example
- "Hear It" button for TTS
- Animated entrance/exit

**`MicrophoneStatus.jsx`**
- Live microphone status indicator
- Animated waveform visualization
- Permission status display
- Pulsing animation when active

---

### Pages (`src/pages/`)

**`Login.jsx`**
- Account type selection (Self vs Parent)
- Login form with mock authentication
- Privacy notice display

**`Dashboard.jsx`**
- User welcome and quick actions
- Stats overview (WPM, accuracy, assists)
- Recent sessions list
- Achievements display

**`Reader.jsx`** ⭐ **Most Complex**
- Reading passage display
- Microphone integration with Web Speech API
- Real-time difficulty detection
- Live WPM counter
- Assist popover trigger
- Font size controls
- Session event logging

**`Reports.jsx`**
- Detailed session analytics
- Session selection sidebar
- Assist timeline with timestamps
- Problem word frequency analysis
- PDF export functionality

**`ParentDashboard.jsx`**
- Child profile cards
- Add child modal
- Per-child session breakdown
- Expandable session details
- PDF report generation per child

---

### Services (`src/services/`)

**`ASRService.js`**
- Web Speech API wrapper
- Continuous speech recognition
- Confidence scoring
- Alternative transcripts
- Error handling

**`DifficultyDetector` class**
- Hesitation detection (pause timing)
- Repeat word detection
- Low confidence flagging
- Phonetic mismatch detection
- Levenshtein distance calculation

**`SimplificationService.js`**
- Mock LLM-style simplification
- Word → simpler alternative mapping
- Explanation generation
- Example sentence creation
- Syllable breakdown
- **NOTE**: Replace with real LLM API in production

**`TTSService.js`**
- Web Speech Synthesis API wrapper
- Voice selection
- Word-by-word timing simulation
- Playback controls (play, pause, stop)
- **NOTE**: Upgrade to cloud TTS for better quality

---

### Context (`src/contexts/`)

**`AuthContext.jsx`**
- User authentication state
- Login/logout functions
- User profile management
- Child profile management (for parents)
- Settings persistence (localStorage)
- Role-based access control

---

## 🎨 Mockup Files (`mockups/`)

**`mockup-1-reader-listening.html`**
- Shows reader in active listening state
- Animated microphone indicator
- Live waveform visualization
- Word highlighting during reading

**`mockup-2-assist-popover.html`**
- Assistance modal design
- Problem word highlighted
- Simplified alternative
- Explanation and example
- Action buttons

**`mockup-3-self-dashboard.html`**
- User dashboard layout
- Quick action cards
- Stats grid
- Recent sessions list
- Achievement badges

**`mockup-4-parent-dashboard.html`**
- Parent dashboard layout
- Multiple child cards
- Selected child sessions
- Expandable session details
- Assist timeline visualization

---

## 🔄 Data Flow

### Reading Session Flow

```
User clicks "Start Reading"
  ↓
Reader.jsx mounts
  ↓
User grants mic permission
  ↓
ASRService initializes Web Speech API
  ↓
User reads aloud
  ↓
ASR captures transcript + confidence
  ↓
DifficultyDetector analyzes:
  - Pause duration
  - Word repeats
  - Confidence score
  - Text mismatch
  ↓
If difficulty detected:
  ↓
SimplificationService called
  ↓
AssistPopover displays:
  - Original word
  - Simplified alternative
  - Explanation
  - Example
  ↓
User clicks "Hear It"
  ↓
TTSService reads with word highlighting
  ↓
Event logged to session history
  ↓
Stats updated (WPM, assist count)
```

### Parent Viewing Child Reports

```
Parent logs in
  ↓
ParentDashboard.jsx loads
  ↓
Displays all children from user.children
  ↓
Parent selects child
  ↓
Fetch child's sessions (mock data)
  ↓
Display session cards
  ↓
Parent expands session
  ↓
Show detailed metrics:
  - WPM, accuracy, duration
  - Problem words
  - Assist timeline with markers
  ↓
Parent clicks "Download Report"
  ↓
jsPDF generates PDF with:
  - Child info
  - Summary stats
  - Session details
  - Problem word list
```

---

## 🔐 Authentication Flow

```
User visits app
  ↓
Redirected to /login
  ↓
Choose Self or Parent account
  ↓
Enter credentials (mock auth)
  ↓
AuthContext.login() called
  ↓
User object created:
  - id, email, name, role
  - settings (font, mic thresholds)
  - children array (if parent)
  ↓
Saved to localStorage
  ↓
Navigate to /dashboard
  ↓
Protected routes now accessible
```

---

## 🎯 Key Features by File

| Feature | Primary File | Supporting Files |
|---------|--------------|------------------|
| **Microphone Listening** | `Reader.jsx` | `ASRService.js`, `MicrophoneStatus.jsx` |
| **Difficulty Detection** | `ASRService.js` (DifficultyDetector) | `Reader.jsx` |
| **Word Simplification** | `SimplificationService.js` | `AssistPopover.jsx` |
| **Text-to-Speech** | `TTSService.js` | `AssistPopover.jsx`, `Reader.jsx` |
| **User Authentication** | `AuthContext.jsx` | `Login.jsx`, `App.jsx` |
| **Session Reports** | `Reports.jsx` | `Dashboard.jsx`, `ParentDashboard.jsx` |
| **PDF Export** | `Reports.jsx`, `ParentDashboard.jsx` | jsPDF library |
| **Parent-Child Management** | `ParentDashboard.jsx` | `AuthContext.jsx` |

---

## 🚀 Getting Started

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Run development server**:
   ```bash
   npm run dev
   ```

3. **View mockups**:
   - Open `mockups/*.html` files directly in browser

4. **Test microphone**:
   - Navigate to Reader page
   - Grant microphone permission
   - Start reading aloud

---

## 📝 Development Notes

### Adding New Passages

Edit `src/pages/Reader.jsx`:
```javascript
const SAMPLE_PASSAGES = [
  {
    id: 1,
    title: 'Your Title',
    content: 'Your passage text here...',
    difficulty: 'beginner', // beginner | intermediate | advanced
  }
];
```

### Adjusting Detection Sensitivity

Edit `src/services/ASRService.js`:
```javascript
new DifficultyDetector({
  hesitationThreshold: 1.5,  // Increase for less sensitive
  repeatThreshold: 3,        // Require more repeats
  confidenceThreshold: 0.5,  // Lower for stricter
});
```

### Adding New Simplifications

Edit `src/services/SimplificationService.js`:
```javascript
this.simplificationDatabase = {
  'yourword': {
    simple: 'easierword',
    explanation: 'What it means...',
    example: 'Example sentence here.',
  }
};
```

---

## 🐛 Debugging Tips

### Microphone Not Detecting Speech
1. Check browser console for errors
2. Verify `ASRService.isSupported` returns true
3. Test with different browsers (Chrome recommended)
4. Check system mic settings

### Assistance Not Triggering
1. Add `console.log` in `detectDifficulties()` function
2. Lower `hesitationThreshold` temporarily
3. Use manual help button (?) to test popover
4. Check event log in browser console

### PDF Not Generating
1. Ensure jsPDF is installed: `npm install jspdf`
2. Check browser console for errors
3. Test with smaller data sets first

---

## 🎓 Learning Resources

- **Web Speech API**: [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
- **React Router**: [Official Docs](https://reactrouter.com/)
- **Framer Motion**: [Animation Guide](https://www.framer.com/motion/)
- **Tailwind CSS**: [Utility Classes](https://tailwindcss.com/docs)
- **jsPDF**: [PDF Generation](https://github.com/parallax/jsPDF)

---

**Built with ❤️ for accessible education**
