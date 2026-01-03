import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  LANG_DB: D1Database;
  LANG_CACHE: KVNamespace;
  LANG_STORAGE: R2Bucket;
  AI: any;
  LANG_VECTORS: VectorizeIndex;
}

// ==============================================================================
// NOIZYLAB OS - PROGRAMMING LANGUAGES WORKER
// Every Programming Language Since The Dawn of Computing
// ==============================================================================

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// ==============================================================================
// COMPLETE PROGRAMMING LANGUAGES DATABASE - FROM 1950s TO PRESENT
// ==============================================================================

const PROGRAMMING_LANGUAGES = {
  // ===========================================================================
  // PIONEERING ERA (1950s)
  // ===========================================================================
  pioneering: {
    fortran: {
      name: 'FORTRAN',
      fullName: 'FORmula TRANslation',
      year: 1957,
      designer: 'John Backus',
      company: 'IBM',
      paradigm: ['Imperative', 'Procedural'],
      typing: 'Static',
      significance: 'First high-level programming language',
      useCases: ['Scientific computing', 'Numerical analysis', 'Supercomputers'],
      modernVersions: ['Fortran 77', 'Fortran 90', 'Fortran 95', 'Fortran 2003', 'Fortran 2008', 'Fortran 2018', 'Fortran 2023'],
      stillUsed: true,
      helloWorld: 'WRITE(*,*) "Hello, World!"'
    },
    lisp: {
      name: 'LISP',
      fullName: 'LISt Processor',
      year: 1958,
      designer: 'John McCarthy',
      institution: 'MIT',
      paradigm: ['Functional', 'Procedural', 'Meta-programming'],
      typing: 'Dynamic',
      significance: 'Second oldest high-level language, pioneered many concepts',
      innovations: ['Garbage collection', 'Tree data structures', 'Dynamic typing', 'Recursion', 'Conditionals'],
      dialects: ['Common Lisp', 'Scheme', 'Clojure', 'Racket', 'Emacs Lisp'],
      helloWorld: '(print "Hello, World!")'
    },
    cobol: {
      name: 'COBOL',
      fullName: 'COmmon Business-Oriented Language',
      year: 1959,
      designer: 'Grace Hopper (influenced)',
      organization: 'CODASYL',
      paradigm: ['Imperative', 'Procedural', 'Object-oriented (2002)'],
      typing: 'Static',
      significance: 'Business/finance standard, still runs banking systems',
      estimatedCodebase: '220 billion lines still in production',
      stillUsed: true,
      helloWorld: 'DISPLAY "Hello, World!".'
    },
    algol: {
      name: 'ALGOL',
      fullName: 'ALGOrithmic Language',
      year: 1958,
      versions: ['ALGOL 58', 'ALGOL 60', 'ALGOL 68'],
      organization: 'ACM/GAMM',
      paradigm: ['Imperative', 'Structured'],
      significance: 'Hugely influential - ancestor of C, Pascal, and many others',
      innovations: ['Block structure', 'Lexical scoping', 'BNF notation', 'Call by name/value']
    }
  },

  // ===========================================================================
  // FOUNDATIONAL ERA (1960s)
  // ===========================================================================
  foundational: {
    basic: {
      name: 'BASIC',
      fullName: 'Beginners All-purpose Symbolic Instruction Code',
      year: 1964,
      designers: ['John Kemeny', 'Thomas Kurtz'],
      institution: 'Dartmouth College',
      paradigm: ['Imperative', 'Procedural'],
      significance: 'Made programming accessible to non-scientists',
      variants: ['GW-BASIC', 'QuickBASIC', 'Visual Basic', 'VB.NET', 'FreeBASIC'],
      helloWorld: 'PRINT "Hello, World!"'
    },
    pl_i: {
      name: 'PL/I',
      year: 1964,
      designer: 'IBM',
      paradigm: ['Imperative', 'Procedural', 'Structured'],
      significance: 'Attempted to combine features of FORTRAN, COBOL, ALGOL'
    },
    simula: {
      name: 'Simula',
      year: 1967,
      designers: ['Ole-Johan Dahl', 'Kristen Nygaard'],
      institution: 'Norwegian Computing Center',
      paradigm: ['Object-oriented', 'Procedural'],
      significance: 'FIRST object-oriented language - invented OOP',
      innovations: ['Classes', 'Objects', 'Inheritance', 'Subclasses']
    },
    logo: {
      name: 'Logo',
      year: 1967,
      designers: ['Wally Feurzeig', 'Seymour Papert'],
      paradigm: ['Functional', 'Educational'],
      significance: 'Educational programming, turtle graphics'
    },
    bcpl: {
      name: 'BCPL',
      fullName: 'Basic Combined Programming Language',
      year: 1967,
      designer: 'Martin Richards',
      significance: 'Influenced B and C'
    },
    b: {
      name: 'B',
      year: 1969,
      designer: 'Ken Thompson',
      company: 'Bell Labs',
      significance: 'Direct predecessor to C'
    },
    forth: {
      name: 'Forth',
      year: 1970,
      designer: 'Chuck Moore',
      paradigm: ['Stack-based', 'Procedural'],
      significance: 'Unique stack-based language, still used in embedded systems'
    }
  },

  // ===========================================================================
  // STRUCTURED PROGRAMMING ERA (1970s)
  // ===========================================================================
  structured: {
    pascal: {
      name: 'Pascal',
      year: 1970,
      designer: 'Niklaus Wirth',
      paradigm: ['Imperative', 'Structured'],
      typing: 'Static, Strong',
      significance: 'Educational language, promoted structured programming',
      derivatives: ['Object Pascal', 'Delphi', 'Free Pascal'],
      helloWorld: "writeln('Hello, World!');"
    },
    c: {
      name: 'C',
      year: 1972,
      designer: 'Dennis Ritchie',
      company: 'Bell Labs',
      paradigm: ['Imperative', 'Procedural', 'Structured'],
      typing: 'Static, Weak',
      significance: 'Most influential language ever - OS, embedded, everywhere',
      useCases: ['Operating systems', 'Embedded systems', 'Compilers', 'Databases'],
      standards: ['K&R C', 'ANSI C (C89)', 'C99', 'C11', 'C17', 'C23'],
      helloWorld: 'printf("Hello, World!\\n");'
    },
    smalltalk: {
      name: 'Smalltalk',
      year: 1972,
      designers: ['Alan Kay', 'Dan Ingalls', 'Adele Goldberg'],
      company: 'Xerox PARC',
      paradigm: ['Object-oriented', 'Reflective'],
      typing: 'Dynamic',
      significance: 'Pure OOP, GUI pioneer, influenced everything',
      innovations: ['Pure OO', 'IDE concept', 'MVC pattern', 'JIT compilation'],
      helloWorld: "Transcript show: 'Hello, World!'"
    },
    prolog: {
      name: 'Prolog',
      fullName: 'PROgramming in LOGic',
      year: 1972,
      designers: ['Alain Colmerauer', 'Robert Kowalski'],
      paradigm: ['Logic', 'Declarative'],
      significance: 'Logic programming pioneer, AI applications',
      helloWorld: "?- write('Hello, World!'), nl."
    },
    ml: {
      name: 'ML',
      fullName: 'Meta Language',
      year: 1973,
      designer: 'Robin Milner',
      institution: 'University of Edinburgh',
      paradigm: ['Functional', 'Imperative'],
      typing: 'Static, Strong, Inferred',
      significance: 'Type inference pioneer',
      dialects: ['Standard ML', 'OCaml', 'F#']
    },
    scheme: {
      name: 'Scheme',
      year: 1975,
      designers: ['Guy Steele', 'Gerald Sussman'],
      institution: 'MIT',
      paradigm: ['Functional', 'Procedural'],
      significance: 'Minimalist Lisp dialect, educational standard'
    },
    sql: {
      name: 'SQL',
      fullName: 'Structured Query Language',
      year: 1974,
      designers: ['Donald Chamberlin', 'Raymond Boyce'],
      company: 'IBM',
      paradigm: ['Declarative', 'Query'],
      significance: 'Universal database language',
      standards: ['SQL-86', 'SQL-92', 'SQL:1999', 'SQL:2003', 'SQL:2008', 'SQL:2011', 'SQL:2016', 'SQL:2019'],
      helloWorld: "SELECT 'Hello, World!';"
    },
    awk: {
      name: 'AWK',
      year: 1977,
      designers: ['Alfred Aho', 'Peter Weinberger', 'Brian Kernighan'],
      company: 'Bell Labs',
      paradigm: ['Data-driven', 'Procedural'],
      significance: 'Text processing pioneer'
    },
    shell: {
      name: 'Bourne Shell',
      year: 1977,
      designer: 'Stephen Bourne',
      company: 'Bell Labs',
      significance: 'UNIX shell scripting standard',
      derivatives: ['bash', 'zsh', 'ksh', 'fish']
    }
  },

  // ===========================================================================
  // OBJECT-ORIENTED ERA (1980s)
  // ===========================================================================
  objectOriented: {
    cpp: {
      name: 'C++',
      year: 1983,
      designer: 'Bjarne Stroustrup',
      company: 'Bell Labs',
      paradigm: ['Multi-paradigm', 'Object-oriented', 'Generic', 'Functional'],
      typing: 'Static, Strong',
      significance: 'Dominant systems language for decades',
      useCases: ['Games', 'Browsers', 'Databases', 'Operating systems', 'Embedded'],
      standards: ['C++98', 'C++03', 'C++11', 'C++14', 'C++17', 'C++20', 'C++23'],
      helloWorld: 'std::cout << "Hello, World!" << std::endl;'
    },
    objective_c: {
      name: 'Objective-C',
      year: 1984,
      designers: ['Brad Cox', 'Tom Love'],
      paradigm: ['Object-oriented', 'Reflective'],
      significance: 'Apple/NeXT standard until Swift',
      helloWorld: 'NSLog(@"Hello, World!");'
    },
    common_lisp: {
      name: 'Common Lisp',
      year: 1984,
      organization: 'ANSI',
      paradigm: ['Multi-paradigm', 'Functional', 'Object-oriented'],
      significance: 'Standardized Lisp dialect'
    },
    ada: {
      name: 'Ada',
      year: 1983,
      designer: 'Jean Ichbiah',
      sponsor: 'US Department of Defense',
      paradigm: ['Multi-paradigm', 'Object-oriented', 'Concurrent'],
      typing: 'Static, Strong',
      significance: 'Safety-critical systems standard',
      useCases: ['Aerospace', 'Defense', 'Rail systems', 'Medical devices']
    },
    matlab: {
      name: 'MATLAB',
      year: 1984,
      designer: 'Cleve Moler',
      company: 'MathWorks',
      paradigm: ['Multi-paradigm', 'Imperative', 'Functional'],
      significance: 'Scientific/engineering computing standard'
    },
    eiffel: {
      name: 'Eiffel',
      year: 1986,
      designer: 'Bertrand Meyer',
      paradigm: ['Object-oriented', 'Contract-based'],
      significance: 'Design by Contract pioneer'
    },
    perl: {
      name: 'Perl',
      year: 1987,
      designer: 'Larry Wall',
      paradigm: ['Multi-paradigm', 'Functional', 'Procedural', 'Object-oriented'],
      typing: 'Dynamic',
      significance: '"Swiss army chainsaw", web/sysadmin pioneer',
      helloWorld: 'print "Hello, World!\\n";'
    },
    tcl: {
      name: 'Tcl',
      fullName: 'Tool Command Language',
      year: 1988,
      designer: 'John Ousterhout',
      paradigm: ['Multi-paradigm', 'Functional', 'Procedural'],
      significance: 'Scripting and GUI (Tk)'
    },
    mathematica: {
      name: 'Wolfram Language (Mathematica)',
      year: 1988,
      designer: 'Stephen Wolfram',
      company: 'Wolfram Research',
      paradigm: ['Multi-paradigm', 'Functional', 'Symbolic'],
      significance: 'Symbolic computation leader'
    }
  },

  // ===========================================================================
  // WEB AND SCRIPTING ERA (1990s)
  // ===========================================================================
  webScripting: {
    haskell: {
      name: 'Haskell',
      year: 1990,
      designers: ['Simon Peyton Jones', 'Philip Wadler', 'et al.'],
      paradigm: ['Pure Functional', 'Lazy evaluation'],
      typing: 'Static, Strong, Inferred',
      significance: 'Pure functional programming standard',
      innovations: ['Monads', 'Type classes', 'Lazy evaluation'],
      helloWorld: 'main = putStrLn "Hello, World!"'
    },
    python: {
      name: 'Python',
      year: 1991,
      designer: 'Guido van Rossum',
      paradigm: ['Multi-paradigm', 'Object-oriented', 'Functional', 'Procedural'],
      typing: 'Dynamic, Strong',
      significance: 'Most popular language for AI/ML, general purpose',
      useCases: ['AI/ML', 'Web', 'Scripting', 'Scientific', 'Automation'],
      versions: ['Python 2.x', 'Python 3.x'],
      helloWorld: 'print("Hello, World!")'
    },
    visual_basic: {
      name: 'Visual Basic',
      year: 1991,
      designer: 'Microsoft',
      paradigm: ['Object-based', 'Event-driven'],
      significance: 'Democratized Windows programming'
    },
    lua: {
      name: 'Lua',
      year: 1993,
      designers: ['Roberto Ierusalimschy', 'Luiz Henrique de Figueiredo', 'Waldemar Celes'],
      institution: 'PUC-Rio',
      paradigm: ['Multi-paradigm', 'Scripting'],
      typing: 'Dynamic',
      significance: 'Game scripting standard, embedded language',
      useCases: ['Games', 'Embedded', 'Configuration'],
      helloWorld: 'print("Hello, World!")'
    },
    r: {
      name: 'R',
      year: 1993,
      designers: ['Ross Ihaka', 'Robert Gentleman'],
      paradigm: ['Multi-paradigm', 'Functional', 'Object-oriented'],
      significance: 'Statistics and data analysis standard',
      helloWorld: 'print("Hello, World!")'
    },
    ruby: {
      name: 'Ruby',
      year: 1995,
      designer: 'Yukihiro Matsumoto',
      paradigm: ['Multi-paradigm', 'Object-oriented', 'Functional'],
      typing: 'Dynamic, Strong',
      significance: 'Developer happiness focus, Rails framework',
      helloWorld: 'puts "Hello, World!"'
    },
    java: {
      name: 'Java',
      year: 1995,
      designer: 'James Gosling',
      company: 'Sun Microsystems',
      paradigm: ['Object-oriented', 'Class-based'],
      typing: 'Static, Strong',
      significance: 'Write once run anywhere, enterprise standard',
      useCases: ['Enterprise', 'Android', 'Web backends', 'Big data'],
      versions: ['Java 1.0 to Java 21+'],
      helloWorld: 'System.out.println("Hello, World!");'
    },
    javascript: {
      name: 'JavaScript',
      year: 1995,
      designer: 'Brendan Eich',
      company: 'Netscape',
      paradigm: ['Multi-paradigm', 'Prototype-based', 'Functional'],
      typing: 'Dynamic, Weak',
      significance: 'Language of the web, most deployed language',
      useCases: ['Web frontend', 'Web backend (Node.js)', 'Mobile', 'Desktop'],
      standards: ['ES3', 'ES5', 'ES6/ES2015', 'ES2016-ES2024'],
      helloWorld: 'console.log("Hello, World!");'
    },
    php: {
      name: 'PHP',
      fullName: 'PHP: Hypertext Preprocessor',
      year: 1995,
      designer: 'Rasmus Lerdorf',
      paradigm: ['Multi-paradigm', 'Imperative', 'Object-oriented'],
      typing: 'Dynamic, Weak',
      significance: 'Web development workhorse, WordPress',
      helloWorld: 'echo "Hello, World!";'
    },
    ocaml: {
      name: 'OCaml',
      year: 1996,
      designer: 'Xavier Leroy',
      institution: 'INRIA',
      paradigm: ['Multi-paradigm', 'Functional', 'Object-oriented'],
      typing: 'Static, Strong, Inferred',
      significance: 'Practical ML dialect'
    },
    delphi: {
      name: 'Object Pascal (Delphi)',
      year: 1995,
      company: 'Borland',
      paradigm: ['Object-oriented', 'Imperative'],
      significance: 'RAD development pioneer'
    }
  },

  // ===========================================================================
  // MODERN ERA (2000s)
  // ===========================================================================
  modern2000s: {
    csharp: {
      name: 'C#',
      year: 2000,
      designer: 'Anders Hejlsberg',
      company: 'Microsoft',
      paradigm: ['Multi-paradigm', 'Object-oriented', 'Functional'],
      typing: 'Static, Strong',
      significance: '.NET platform language, Unity game development',
      useCases: ['Enterprise', 'Games (Unity)', 'Web (ASP.NET)', 'Desktop'],
      helloWorld: 'Console.WriteLine("Hello, World!");'
    },
    actionscript: {
      name: 'ActionScript',
      year: 2000,
      company: 'Macromedia/Adobe',
      paradigm: ['Object-oriented', 'Prototype-based'],
      significance: 'Flash platform language (deprecated)'
    },
    groovy: {
      name: 'Groovy',
      year: 2003,
      designer: 'James Strachan',
      paradigm: ['Object-oriented', 'Scripting'],
      significance: 'JVM scripting, Gradle build tool'
    },
    scala: {
      name: 'Scala',
      year: 2004,
      designer: 'Martin Odersky',
      paradigm: ['Multi-paradigm', 'Functional', 'Object-oriented'],
      typing: 'Static, Strong',
      significance: 'JVM functional/OOP hybrid, Spark',
      helloWorld: 'println("Hello, World!")'
    },
    f_sharp: {
      name: 'F#',
      year: 2005,
      company: 'Microsoft',
      designer: 'Don Syme',
      paradigm: ['Functional', 'Object-oriented'],
      typing: 'Static, Strong, Inferred',
      significance: 'Functional .NET language'
    },
    powershell: {
      name: 'PowerShell',
      year: 2006,
      company: 'Microsoft',
      paradigm: ['Object-oriented', 'Functional', 'Pipeline'],
      significance: 'Windows administration standard'
    },
    clojure: {
      name: 'Clojure',
      year: 2007,
      designer: 'Rich Hickey',
      paradigm: ['Functional', 'Concurrent'],
      typing: 'Dynamic, Strong',
      platform: 'JVM, JavaScript',
      significance: 'Modern Lisp, immutability focus',
      helloWorld: '(println "Hello, World!")'
    },
    go: {
      name: 'Go (Golang)',
      year: 2009,
      designers: ['Robert Griesemer', 'Rob Pike', 'Ken Thompson'],
      company: 'Google',
      paradigm: ['Imperative', 'Concurrent'],
      typing: 'Static, Strong',
      significance: 'Cloud infrastructure language, simplicity focus',
      useCases: ['Cloud', 'Infrastructure', 'DevOps', 'CLI tools'],
      helloWorld: 'fmt.Println("Hello, World!")'
    }
  },

  // ===========================================================================
  // CONTEMPORARY ERA (2010s-2020s)
  // ===========================================================================
  contemporary: {
    rust: {
      name: 'Rust',
      year: 2010,
      designer: 'Graydon Hoare',
      company: 'Mozilla',
      paradigm: ['Multi-paradigm', 'Concurrent', 'Functional'],
      typing: 'Static, Strong',
      significance: 'Memory safety without garbage collection',
      innovations: ['Ownership', 'Borrowing', 'Lifetimes', 'Zero-cost abstractions'],
      useCases: ['Systems', 'WebAssembly', 'CLI', 'Embedded', 'Blockchain'],
      helloWorld: 'println!("Hello, World!");'
    },
    kotlin: {
      name: 'Kotlin',
      year: 2011,
      company: 'JetBrains',
      paradigm: ['Multi-paradigm', 'Object-oriented', 'Functional'],
      typing: 'Static, Strong',
      significance: 'Official Android language, better Java',
      platforms: ['JVM', 'JavaScript', 'Native'],
      helloWorld: 'println("Hello, World!")'
    },
    elixir: {
      name: 'Elixir',
      year: 2011,
      designer: 'José Valim',
      paradigm: ['Functional', 'Concurrent'],
      typing: 'Dynamic, Strong',
      platform: 'Erlang VM (BEAM)',
      significance: 'Modern Erlang with Ruby-like syntax',
      helloWorld: 'IO.puts "Hello, World!"'
    },
    typescript: {
      name: 'TypeScript',
      year: 2012,
      company: 'Microsoft',
      designer: 'Anders Hejlsberg',
      paradigm: ['Multi-paradigm', 'Object-oriented', 'Functional'],
      typing: 'Static, Strong, Optional',
      significance: 'JavaScript with types, enterprise JS standard',
      helloWorld: 'console.log("Hello, World!");'
    },
    dart: {
      name: 'Dart',
      year: 2011,
      company: 'Google',
      paradigm: ['Object-oriented', 'Functional'],
      typing: 'Static, Strong',
      significance: 'Flutter framework language',
      helloWorld: "print('Hello, World!');"
    },
    julia: {
      name: 'Julia',
      year: 2012,
      designers: ['Jeff Bezanson', 'Stefan Karpinski', 'Viral Shah', 'Alan Edelman'],
      institution: 'MIT',
      paradigm: ['Multi-paradigm', 'Functional', 'Procedural'],
      typing: 'Dynamic, Strong',
      significance: 'High-performance scientific computing',
      helloWorld: 'println("Hello, World!")'
    },
    swift: {
      name: 'Swift',
      year: 2014,
      company: 'Apple',
      designer: 'Chris Lattner',
      paradigm: ['Multi-paradigm', 'Protocol-oriented', 'Object-oriented', 'Functional'],
      typing: 'Static, Strong',
      significance: 'Modern Apple platform language',
      useCases: ['iOS', 'macOS', 'watchOS', 'tvOS', 'Server'],
      helloWorld: 'print("Hello, World!")'
    },
    hack: {
      name: 'Hack',
      year: 2014,
      company: 'Facebook/Meta',
      paradigm: ['Object-oriented'],
      typing: 'Static/Gradual',
      significance: 'PHP with static typing'
    },
    crystal: {
      name: 'Crystal',
      year: 2014,
      paradigm: ['Object-oriented', 'Functional'],
      typing: 'Static, Strong, Inferred',
      significance: 'Ruby-like syntax with C performance'
    },
    nim: {
      name: 'Nim',
      year: 2008,
      designer: 'Andreas Rumpf',
      paradigm: ['Multi-paradigm'],
      typing: 'Static, Strong',
      significance: 'Python-like syntax, systems performance'
    },
    zig: {
      name: 'Zig',
      year: 2015,
      designer: 'Andrew Kelley',
      paradigm: ['Imperative', 'Systems'],
      typing: 'Static, Strong',
      significance: 'Modern C alternative, no hidden control flow'
    },
    v: {
      name: 'V',
      year: 2019,
      designer: 'Alexander Medvednikov',
      paradigm: ['Multi-paradigm'],
      typing: 'Static, Strong',
      significance: 'Simple, fast, safe systems language'
    },
    carbon: {
      name: 'Carbon',
      year: 2022,
      company: 'Google',
      paradigm: ['Multi-paradigm'],
      typing: 'Static, Strong',
      significance: 'Experimental C++ successor'
    },
    mojo: {
      name: 'Mojo',
      year: 2023,
      company: 'Modular',
      designer: 'Chris Lattner',
      paradigm: ['Multi-paradigm'],
      typing: 'Static, Strong',
      significance: 'Python superset for AI/ML performance'
    }
  },

  // ===========================================================================
  // DOMAIN-SPECIFIC LANGUAGES
  // ===========================================================================
  domainSpecific: {
    vhdl: {
      name: 'VHDL',
      year: 1983,
      significance: 'Hardware description language',
      domain: 'Digital circuit design'
    },
    verilog: {
      name: 'Verilog',
      year: 1984,
      significance: 'Hardware description language',
      domain: 'Digital circuit design'
    },
    systemverilog: {
      name: 'SystemVerilog',
      year: 2002,
      significance: 'Advanced HDL with verification',
      domain: 'Hardware design and verification'
    },
    latex: {
      name: 'LaTeX',
      year: 1984,
      designer: 'Leslie Lamport',
      significance: 'Document typesetting standard',
      domain: 'Academic publishing'
    },
    postscript: {
      name: 'PostScript',
      year: 1982,
      company: 'Adobe',
      significance: 'Page description language',
      domain: 'Printing and graphics'
    },
    regex: {
      name: 'Regular Expressions',
      year: 1956,
      designer: 'Stephen Cole Kleene',
      significance: 'Pattern matching standard',
      domain: 'Text processing'
    },
    graphql: {
      name: 'GraphQL',
      year: 2015,
      company: 'Facebook/Meta',
      significance: 'API query language',
      domain: 'API design'
    },
    protobuf: {
      name: 'Protocol Buffers',
      year: 2001,
      company: 'Google',
      significance: 'Data serialization',
      domain: 'Data interchange'
    },
    yaml: {
      name: 'YAML',
      year: 2001,
      significance: 'Human-readable data serialization',
      domain: 'Configuration'
    },
    json: {
      name: 'JSON',
      year: 2001,
      designer: 'Douglas Crockford',
      significance: 'Data interchange standard',
      domain: 'Web APIs, configuration'
    },
    toml: {
      name: 'TOML',
      year: 2013,
      designer: 'Tom Preston-Werner',
      significance: 'Configuration file format',
      domain: 'Configuration'
    },
    markdown: {
      name: 'Markdown',
      year: 2004,
      designer: 'John Gruber',
      significance: 'Lightweight markup language',
      domain: 'Documentation'
    },
    solidity: {
      name: 'Solidity',
      year: 2014,
      company: 'Ethereum',
      significance: 'Smart contract language',
      domain: 'Blockchain/DeFi'
    },
    move: {
      name: 'Move',
      year: 2019,
      company: 'Meta (Diem/Libra)',
      significance: 'Safe smart contract language',
      domain: 'Blockchain'
    }
  },

  // ===========================================================================
  // ESOTERIC AND EDUCATIONAL LANGUAGES
  // ===========================================================================
  esotericEducational: {
    brainfuck: {
      name: 'Brainfuck',
      year: 1993,
      designer: 'Urban Müller',
      significance: 'Minimalist esoteric language',
      characters: '8 characters only: > < + - . , [ ]'
    },
    lolcode: {
      name: 'LOLCODE',
      year: 2007,
      significance: 'LOLcats-based syntax'
    },
    whitespace: {
      name: 'Whitespace',
      year: 2003,
      significance: 'Only whitespace characters are significant'
    },
    scratch: {
      name: 'Scratch',
      year: 2003,
      institution: 'MIT Media Lab',
      significance: 'Visual programming for education'
    },
    blockly: {
      name: 'Blockly',
      year: 2012,
      company: 'Google',
      significance: 'Visual block-based programming'
    },
    processing: {
      name: 'Processing',
      year: 2001,
      significance: 'Visual arts and design programming'
    },
    p5js: {
      name: 'p5.js',
      year: 2014,
      significance: 'JavaScript version of Processing'
    }
  },

  // ===========================================================================
  // ASSEMBLY LANGUAGES
  // ===========================================================================
  assembly: {
    x86_assembly: {
      name: 'x86 Assembly',
      year: 1978,
      platform: 'Intel 8086 and successors',
      significance: 'PC assembly standard'
    },
    arm_assembly: {
      name: 'ARM Assembly',
      year: 1985,
      platform: 'ARM processors',
      significance: 'Mobile/embedded assembly'
    },
    mips_assembly: {
      name: 'MIPS Assembly',
      year: 1985,
      platform: 'MIPS processors',
      significance: 'Educational and embedded'
    },
    risc_v_assembly: {
      name: 'RISC-V Assembly',
      year: 2010,
      platform: 'RISC-V processors',
      significance: 'Open-source ISA assembly'
    },
    z80_assembly: {
      name: 'Z80 Assembly',
      year: 1976,
      platform: 'Zilog Z80',
      significance: 'Classic 8-bit assembly'
    },
    m6502_assembly: {
      name: '6502 Assembly',
      year: 1975,
      platform: 'MOS 6502',
      significance: 'Apple II, C64, NES assembly'
    }
  },

  // ===========================================================================
  // CONCURRENT/PARALLEL LANGUAGES
  // ===========================================================================
  concurrent: {
    erlang: {
      name: 'Erlang',
      year: 1986,
      company: 'Ericsson',
      designers: ['Joe Armstrong', 'Robert Virding', 'Mike Williams'],
      paradigm: ['Functional', 'Concurrent', 'Distributed'],
      significance: 'Telecom reliability standard, actor model',
      useCases: ['Telecom', 'Messaging (WhatsApp)', 'Distributed systems'],
      helloWorld: 'io:fwrite("Hello, World!~n").'
    },
    occam: {
      name: 'occam',
      year: 1983,
      company: 'INMOS',
      significance: 'CSP-based concurrent language, Transputer'
    },
    chapel: {
      name: 'Chapel',
      year: 2009,
      company: 'Cray',
      significance: 'Parallel programming language'
    },
    x10: {
      name: 'X10',
      year: 2004,
      company: 'IBM',
      significance: 'High-performance parallel computing'
    },
    cuda: {
      name: 'CUDA',
      year: 2007,
      company: 'NVIDIA',
      significance: 'GPU computing standard',
      domain: 'GPU programming'
    },
    opencl: {
      name: 'OpenCL',
      year: 2009,
      organization: 'Khronos Group',
      significance: 'Cross-platform parallel computing'
    }
  }
};

// ==============================================================================
// API ENDPOINTS
// ==============================================================================

// Get all language categories
app.get('/api/languages/categories', (c) => {
  const categories = Object.keys(PROGRAMMING_LANGUAGES);
  return c.json({
    success: true,
    categories,
    totalCategories: categories.length
  });
});

// Search all languages
app.get('/api/languages/search', (c) => {
  const query = (c.req.query('q') || '').toLowerCase();
  const results: any[] = [];

  Object.entries(PROGRAMMING_LANGUAGES).forEach(([category, languages]) => {
    Object.entries(languages).forEach(([key, lang]: [string, any]) => {
      const name = lang.name || key;
      const fullName = lang.fullName || '';
      const designer = lang.designer || lang.designers?.join(', ') || '';
      const significance = lang.significance || '';

      if (
        name.toLowerCase().includes(query) ||
        fullName.toLowerCase().includes(query) ||
        designer.toLowerCase().includes(query) ||
        significance.toLowerCase().includes(query)
      ) {
        results.push({ category, key, ...lang });
      }
    });
  });

  return c.json({
    success: true,
    query,
    resultCount: results.length,
    results
  });
});

// Get language by category
app.get('/api/languages/category/:category', (c) => {
  const category = c.req.param('category') as keyof typeof PROGRAMMING_LANGUAGES;
  const data = PROGRAMMING_LANGUAGES[category];

  if (!data) {
    return c.json({ error: 'Category not found' }, 404);
  }

  return c.json({
    success: true,
    category,
    languages: data
  });
});

// Get specific language
app.get('/api/languages/:key', (c) => {
  const key = c.req.param('key').toLowerCase();
  let found: any = null;
  let foundCategory: string = '';

  Object.entries(PROGRAMMING_LANGUAGES).forEach(([category, languages]) => {
    Object.entries(languages).forEach(([langKey, lang]) => {
      if (langKey.toLowerCase() === key || (lang as any).name?.toLowerCase() === key) {
        found = lang;
        foundCategory = category;
      }
    });
  });

  if (!found) {
    return c.json({ error: 'Language not found' }, 404);
  }

  return c.json({
    success: true,
    category: foundCategory,
    language: found
  });
});

// Get timeline
app.get('/api/languages/timeline', (c) => {
  const timeline: { year: number; name: string; category: string; significance?: string }[] = [];

  Object.entries(PROGRAMMING_LANGUAGES).forEach(([category, languages]) => {
    Object.entries(languages).forEach(([key, lang]: [string, any]) => {
      if (lang.year) {
        timeline.push({
          year: lang.year,
          name: lang.name || key,
          category,
          significance: lang.significance
        });
      }
    });
  });

  timeline.sort((a, b) => a.year - b.year);

  return c.json({
    success: true,
    totalEntries: timeline.length,
    timeline
  });
});

// Get languages by paradigm
app.get('/api/languages/paradigm/:paradigm', (c) => {
  const paradigm = c.req.param('paradigm').toLowerCase();
  const results: any[] = [];

  Object.entries(PROGRAMMING_LANGUAGES).forEach(([category, languages]) => {
    Object.entries(languages).forEach(([key, lang]: [string, any]) => {
      if (lang.paradigm && lang.paradigm.some((p: string) => p.toLowerCase().includes(paradigm))) {
        results.push({ category, key, ...lang });
      }
    });
  });

  return c.json({
    success: true,
    paradigm,
    resultCount: results.length,
    languages: results
  });
});

// Get languages by typing system
app.get('/api/languages/typing/:type', (c) => {
  const typingType = c.req.param('type').toLowerCase();
  const results: any[] = [];

  Object.entries(PROGRAMMING_LANGUAGES).forEach(([category, languages]) => {
    Object.entries(languages).forEach(([key, lang]: [string, any]) => {
      if (lang.typing && lang.typing.toLowerCase().includes(typingType)) {
        results.push({ category, key, ...lang });
      }
    });
  });

  return c.json({
    success: true,
    typingType,
    resultCount: results.length,
    languages: results
  });
});

// Get hello world examples
app.get('/api/languages/hello-world', (c) => {
  const examples: { language: string; code: string }[] = [];

  Object.entries(PROGRAMMING_LANGUAGES).forEach(([_, languages]) => {
    Object.entries(languages).forEach(([key, lang]: [string, any]) => {
      if (lang.helloWorld) {
        examples.push({
          language: lang.name || key,
          code: lang.helloWorld
        });
      }
    });
  });

  return c.json({
    success: true,
    totalExamples: examples.length,
    examples
  });
});

// AI-powered language recommendation
app.post('/api/languages/recommend', async (c) => {
  const { useCase, experience, requirements } = await c.req.json();

  const prompt = `Based on this use case: "${useCase}"
Developer experience: ${experience}
Requirements: ${JSON.stringify(requirements)}

Recommend the best programming language(s) and explain why.
Consider: performance, ecosystem, learning curve, job market, and community.`;

  const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
    prompt,
    max_tokens: 1000
  });

  return c.json({
    success: true,
    recommendation: response.response
  });
});

// Get statistics
app.get('/api/languages/stats', (c) => {
  let totalLanguages = 0;
  const byCategory: Record<string, number> = {};
  const byDecade: Record<string, number> = {};
  const byParadigm: Record<string, number> = {};

  Object.entries(PROGRAMMING_LANGUAGES).forEach(([category, languages]) => {
    const count = Object.keys(languages).length;
    byCategory[category] = count;
    totalLanguages += count;

    Object.entries(languages).forEach(([_, lang]: [string, any]) => {
      if (lang.year) {
        const decade = `${Math.floor(lang.year / 10) * 10}s`;
        byDecade[decade] = (byDecade[decade] || 0) + 1;
      }
      if (lang.paradigm) {
        lang.paradigm.forEach((p: string) => {
          byParadigm[p] = (byParadigm[p] || 0) + 1;
        });
      }
    });
  });

  return c.json({
    success: true,
    totalLanguages,
    byCategory,
    byDecade: Object.fromEntries(Object.entries(byDecade).sort()),
    byParadigm: Object.fromEntries(Object.entries(byParadigm).sort((a, b) => b[1] - a[1]))
  });
});

// Health check
app.get('/health', (c) => {
  return c.json({
    status: 'healthy',
    worker: 'programming-languages-worker',
    version: '1.0.0',
    timestamp: new Date().toISOString(),
    capabilities: [
      'Every programming language since FORTRAN (1957)',
      'Pioneering era languages (1950s)',
      'Foundational languages (1960s)',
      'Structured programming era (1970s)',
      'Object-oriented era (1980s)',
      'Web and scripting era (1990s)',
      'Modern languages (2000s)',
      'Contemporary languages (2010s-2020s)',
      'Domain-specific languages',
      'Esoteric and educational languages',
      'Assembly languages',
      'Concurrent/parallel languages',
      'Hello World examples',
      'AI-powered recommendations'
    ]
  });
});

export default app;
