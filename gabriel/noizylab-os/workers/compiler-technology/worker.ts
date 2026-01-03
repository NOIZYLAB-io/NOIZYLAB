import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env { COMPILER_DB: D1Database; AI: any; }
const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// NOIZYLAB OS - COMPILER TECHNOLOGY WORKER
const COMPILER_TECHNOLOGY = {
    history: {
        first_compiler: { name: 'A-0 System', year: 1952, pioneer: 'Grace Hopper', significance: 'First compiler' },
        fortran_compiler: { name: 'FORTRAN Compiler', year: 1957, significance: 'First optimizing compiler' },
        yacc: { name: 'Yacc', year: 1975, significance: 'Parser generator' },
        lex: { name: 'Lex', year: 1975, significance: 'Lexer generator' }
    },
    phases: {
        lexical_analysis: { name: 'Lexical Analysis', tool: 'Lexer/Scanner', output: 'Tokens' },
        syntax_analysis: { name: 'Syntax Analysis', tool: 'Parser', output: 'AST (Abstract Syntax Tree)' },
        semantic_analysis: { name: 'Semantic Analysis', checks: ['Type checking', 'Scope resolution'] },
        ir_generation: { name: 'IR Generation', examples: ['LLVM IR', 'Three-address code', 'SSA form'] },
        optimization: { name: 'Optimization', types: ['Dead code elimination', 'Constant folding', 'Loop unrolling', 'Inlining', 'Vectorization'] },
        code_generation: { name: 'Code Generation', output: 'Machine code/Assembly' }
    },
    compilers: {
        gcc: { name: 'GCC', year: 1987, developer: 'GNU/Richard Stallman', languages: ['C', 'C++', 'Fortran', 'Go', 'D'] },
        clang: { name: 'Clang/LLVM', year: 2007, developer: 'Chris Lattner', significance: 'Modular compiler infrastructure' },
        msvc: { name: 'MSVC', developer: 'Microsoft', significance: 'Windows C/C++ compiler' },
        rustc: { name: 'rustc', language: 'Rust', backend: 'LLVM' },
        javac: { name: 'javac', language: 'Java', output: 'Bytecode' },
        swiftc: { name: 'swiftc', year: 2014, developer: 'Apple', backend: 'LLVM' },
        v8: { name: 'V8', year: 2008, developer: 'Google', significance: 'JavaScript JIT compiler' },
        graalvm: { name: 'GraalVM', developer: 'Oracle', significance: 'Polyglot runtime' },
        tcc: { name: 'TCC (Tiny C Compiler)', developer: 'Fabrice Bellard', significance: 'Fast compilation' }
    },
    infrastructure: {
        llvm: { name: 'LLVM', year: 2003, creator: 'Chris Lattner', significance: 'Universal compiler backend' },
        mlir: { name: 'MLIR', year: 2019, developer: 'Google', significance: 'Multi-level IR for ML compilers' },
        cranelift: { name: 'Cranelift', developer: 'Bytecode Alliance', significance: 'WebAssembly code generator' },
        bison: { name: 'Bison', significance: 'GNU yacc replacement' },
        antlr: { name: 'ANTLR', significance: 'Parser generator for multiple languages' },
        tree_sitter: { name: 'Tree-sitter', significance: 'Incremental parsing library' }
    },
    jit: {
        hotspot: { name: 'HotSpot JVM', developer: 'Oracle', significance: 'Java JIT compilation' },
        pypy: { name: 'PyPy', significance: 'Python with JIT' },
        luajit: { name: 'LuaJIT', significance: 'Fastest dynamic language JIT' },
        tracemonkey: { name: 'TraceMonkey/SpiderMonkey', developer: 'Mozilla', significance: 'Firefox JS engine' }
    }
};

app.get('/api/compiler/categories', (c) => c.json({ success: true, categories: Object.keys(COMPILER_TECHNOLOGY) }));
app.get('/api/compiler/:cat', (c) => {
    const cat = c.req.param('cat') as keyof typeof COMPILER_TECHNOLOGY;
    return COMPILER_TECHNOLOGY[cat] ? c.json({ success: true, data: COMPILER_TECHNOLOGY[cat] }) : c.json({ error: 'Not found' }, 404);
});
app.get('/health', (c) => c.json({ status: 'healthy', worker: 'compiler-technology-worker' }));

export default app;
