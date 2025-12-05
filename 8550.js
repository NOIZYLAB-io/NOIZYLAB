try{let a="undefined"!=typeof window?window:"undefined"!=typeof global?global:"undefined"!=typeof globalThis?globalThis:"undefined"!=typeof self?self:{},b=(new a.Error).stack;b&&(a._sentryDebugIds=a._sentryDebugIds||{},a._sentryDebugIds[b]="f4b8e77b-d1a5-4347-ab84-24547d6af9dc",a._sentryDebugIdIdentifier="sentry-dbid-f4b8e77b-d1a5-4347-ab84-24547d6af9dc")}catch(a){}exports.id=8550,exports.ids=[8550],exports.modules={13234:(a,b,c)=>{"use strict";c.a(a,async(a,d)=>{try{c.d(b,{$W:()=>p,DV:()=>q,FI:()=>n,Hv:()=>u,jM:()=>o,mf:()=>r,mm:()=>t,ns:()=>s,vz:()=>v});var e=c(23554),f=c(39040),g=a([e]);function h(a){return e.A.prepare("SELECT * FROM connection WHERE provider = ?").get((0,f.pJ)(a))}e=(g.then?(await g)():g)[0];let n={upsert:function(a){let b=h(a.provider)||{};return{id:e.A.prepare(`
    INSERT INTO connection (provider, apikey, organization_id, custom_link, google_Oauth, region, access_key_id, secret_access_key, session_token)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(provider) DO UPDATE SET
      apikey = COALESCE(excluded.apikey, connection.apikey),
      organization_id = COALESCE(excluded.organization_id, connection.organization_id),
      custom_link = COALESCE(excluded.custom_link, connection.custom_link),
      google_Oauth = COALESCE(excluded.google_Oauth, connection.google_Oauth),
      region = COALESCE(excluded.region, connection.region),
      access_key_id = COALESCE(excluded.access_key_id, connection.access_key_id),
      secret_access_key = COALESCE(excluded.secret_access_key, connection.secret_access_key),
      session_token = COALESCE(excluded.session_token, connection.session_token),
      updated_at = CURRENT_TIMESTAMP
  `).run((0,f.pJ)(a.provider),a.apikey??b.apikey,a.organization_id??b.organization_id,a.custom_link??b.custom_link,a.google_Oauth??b.google_Oauth,a.region??b.region,a.access_key_id??b.access_key_id,a.secret_access_key??b.secret_access_key,a.session_token??b.session_token).lastInsertRowid,...a,created_at:b.created_at??new Date().toISOString(),updated_at:new Date().toISOString()}},getByProvider:h,getAll:function(){return e.A.prepare("SELECT * FROM connection").all()},delete:function(a){e.A.prepare("DELETE FROM connection WHERE provider = ?").run((0,f.pJ)(a))}};function i(){return e.A.prepare("SELECT * FROM codegpt_session LIMIT 1").get()}let o={upsert:function(a){let b=i()||{};e.A.prepare(`
    INSERT INTO codegpt_session (id, access_token, refresh_token, expires_at, signed_distinct_id, distinct_id) 
    VALUES (1, ?, ?, ?, ?, ?)
    ON CONFLICT(id) DO UPDATE SET
      access_token = excluded.access_token,
      refresh_token = excluded.refresh_token,
      expires_at = excluded.expires_at,
      signed_distinct_id = excluded.signed_distinct_id,
      distinct_id = excluded.distinct_id,
      updated_at = CURRENT_TIMESTAMP
  `).run(a.access_token??b.access_token,a.refresh_token??b.refresh_token,a.expires_at??b.expires_at,a.signed_distinct_id??b.signed_distinct_id,a.distinct_id??b.distinct_id)},get:i,delete:function(){e.A.prepare("DELETE FROM codegpt_session").run()}};function j(a){return e.A.prepare("SELECT * FROM settings WHERE provider = ?").get((0,f.pJ)(a))??{provider:a,memory:10,temperature:0,max_tokens:512}}let p={upsert:function(a){let b=j((0,f.pJ)(a.provider))||{};return{id:e.A.prepare(`
    INSERT INTO settings (provider, memory, temperature, max_tokens)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(provider) DO UPDATE SET
      memory = COALESCE(excluded.memory, settings.memory),
      temperature = COALESCE(excluded.temperature, settings.temperature),
      max_tokens = COALESCE(excluded.max_tokens, settings.max_tokens),
      updated_at = CURRENT_TIMESTAMP
  `).run((0,f.pJ)(a.provider),a.memory??b.memory,a.temperature??b.temperature,a.max_tokens??b.max_tokens).lastInsertRowid,provider:a.provider,memory:a.memory??b.memory,temperature:a.temperature??b.temperature,max_tokens:a.max_tokens??b.max_tokens,created_at:b.created_at??new Date().toISOString(),updated_at:new Date().toISOString()}},getByProvider:j,getAll:function(){return e.A.prepare("SELECT * FROM settings").all()},delete:function(a){e.A.prepare("DELETE FROM settings WHERE provider = ?").run((0,f.pJ)(a))}};function k(){let a=e.A.prepare("SELECT * FROM auto_complete LIMIT 1").get();return a||{enabled:1,provider:"codegptplus",model:"Plus",max_tokens:300,delay:200}}let q={upsert:function(a){let b=k();e.A.prepare(`
    INSERT OR REPLACE INTO auto_complete (id, enabled, provider, model, max_tokens, delay, created_at, updated_at)
    VALUES (1, ?, ?, ?, ?, ?, COALESCE(?, CURRENT_TIMESTAMP), CURRENT_TIMESTAMP)
  `).run(a.enabled??b.enabled,(0,f.pJ)(a.provider||b.provider),a.model??b.model,a.max_tokens??b.max_tokens,a.delay??b.delay,b.created_at)},get:k,delete:function(){e.A.prepare("DELETE FROM auto_complete").run()}};function l(){return e.A.prepare("SELECT * FROM auto_select LIMIT 1").get()}let r={upsert:function(a){let b=l()||{};e.A.prepare(`
    INSERT OR REPLACE INTO auto_select (id, enabled, created_at, updated_at)
    VALUES (1, ?, COALESCE(?, CURRENT_TIMESTAMP), CURRENT_TIMESTAMP)
  `).run(a.enabled??b.enabled,b.created_at)},get:l,delete:function(){e.A.prepare("DELETE FROM auto_select").run()}};function m(a){return e.A.prepare("SELECT * FROM history WHERE id = ?").get(a)}let s={upsert:function(a){let b=m(a.id)||{},c=e.A.prepare(`
    INSERT INTO history (id, name)
    VALUES (?, ?)
    ON CONFLICT(id) DO UPDATE SET
      name = COALESCE(excluded.name, history.name),
      updated_at = CURRENT_TIMESTAMP
  `).run(a.id??b.id,a.name??b.name);return{id:a.id??c.lastInsertRowid.toString(),...a,created_at:b.created_at??new Date().toISOString(),updated_at:new Date().toISOString()}},getById:m,getAll:function(){return e.A.prepare("SELECT * FROM history ORDER BY id DESC").all()},getEmpty:function(){return e.A.prepare(`
    SELECT h.*
    FROM history h
    LEFT JOIN message m ON h.id = m.history_id
    WHERE m.id IS NULL
    ORDER BY h.id ASC
    LIMIT 1
  `).get()},delete:function(a){e.A.prepare("DELETE FROM message WHERE history_id = ?").run(a),e.A.prepare("DELETE FROM history WHERE id = ?").run(a)}},t={upsert:function(a){let b=e.A.prepare(`
    INSERT OR REPLACE INTO message (id, content, display, message_index, history_id, role, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, ?, COALESCE(?, CURRENT_TIMESTAMP), CURRENT_TIMESTAMP)
  `).run(a.id,a.content,a.display,a.message_index,a.history_id,a.role??"user",a.created_at);return{id:a.id??b.lastInsertRowid.toString(),...a,created_at:a.created_at??new Date().toISOString(),updated_at:new Date().toISOString()}},getById:function(a){return e.A.prepare("SELECT * FROM message WHERE id = ?").get(a)},getAll:function(){return e.A.prepare("SELECT * FROM message ORDER BY id DESC").all()},getAllByHistoryId:function(a){return e.A.prepare('SELECT * FROM message WHERE history_id = ? ORDER BY "message_index" ASC').all(a)},delete:function(a){e.A.prepare("DELETE FROM message WHERE id = ?").run(a)}},u={upsert:function(a){e.A.prepare(`
    INSERT INTO kv (key, value)
    VALUES (?, ?)
    ON CONFLICT(key) DO UPDATE SET
      value = excluded.value
  `).run(a.key,JSON.stringify(a.value))},get:function(a){let b=e.A.prepare("SELECT * FROM kv WHERE key = ?").get(a);if(b)return JSON.parse(b.value||"")},getAll:function(){return e.A.prepare("SELECT * FROM kv").all().map(a=>({key:a.key,value:JSON.parse(a.value)}))},delete:function(a){e.A.prepare("DELETE FROM kv WHERE key = ?").run(a)}},v={upsert:function(a){let b=Math.floor(333);for(let c=0;c<a.length;c+=b){let d=a.slice(c,c+b),f=d.map(()=>"(?, ?, ?)").join(", "),g=e.A.prepare(`
      INSERT OR REPLACE INTO file_hashes (origin_file, workspace_id, hash)
      VALUES ${f}
    `),h=d.flatMap(a=>[a.origin_file,a.workspace_id,a.hash]);g.run(...h)}},get:function(a){return e.A.prepare("SELECT * FROM file_hashes WHERE workspace_id = ? ").all(a)},hasHashes:function(a){return e.A.prepare("SELECT * FROM file_hashes WHERE workspace_id = ? LIMIT 1").all(a).length>0},getByOriginFile:function(a,b){return e.A.prepare("SELECT hash FROM file_hashes WHERE workspace_id = ? AND origin_file = ?").all(a,b)},delete:function(a,b){if(0===b.length)return;let c=b.map(()=>"?").join(",");e.A.prepare(`DELETE FROM file_hashes WHERE workspace_id = ? AND hash IN (${c})`).run(a,...b)},deleteAll:function(a){e.A.prepare("DELETE FROM file_hashes WHERE workspace_id = ?").run(a)}};d()}catch(a){d(a)}})},23554:(a,b,c)=>{"use strict";c.a(a,async(a,d)=>{try{c.d(b,{A:()=>a});var e=c(98498),f=c(91912),g=c.n(f),h=c(79748),i=c.n(h),j=c(21820),k=c.n(j),l=c(33873),m=c.n(l);async function n(a="db.sqlite",b=".codegpt",c="qb98QNQptnRmXb"){try{let d=k().homedir(),f=m().join(d,b),h=m().join(f,a);await i().mkdir(f,{recursive:!0});let j=new(g())(h);return j.pragma(`key = '${c}'`),j.pragma("journal_mode = WAL"),(0,e.A)(j),j}catch(a){throw console.error(`Error initializing database: ${a.message}`),a}}let a=await n();d()}catch(a){d(a)}},1)},39040:(a,b,c)=>{"use strict";c.d(b,{B2:()=>e,GT:()=>k,pJ:()=>d,tX:()=>g,yh:()=>i,zf:()=>j});let d=a=>a.toLowerCase().replaceAll(" ",""),e=process.env.NEXT_PUBLIC_IDE??"vscode",f="http://localhost:54112",g=async a=>{try{let b=await fetch("https://storage.codegpt.co/vscode/providers2.json"),c=(await b.json()).find(b=>b.link===a);return c?.tools?.map(a=>({type:"function",function:{name:a.name,description:a.description,parameters:a.parameters}}))}catch(b){return console.error(`Error fetching ${a} tools:`,b),[]}},h=async()=>{try{let a=await fetch(`${f}/api/fetch-data/providers`);if(!a.ok)return{ok:!1,json:[]};let b=await a.json();return{ok:a.ok,json:b}}catch(a){return console.error("Failed to fetch providers:",a),{ok:!1,json:[]}}},i=async({provider:a,model:b})=>{let c=await h(),d=(await c.json).find(b=>b.link===a),e=d?.prompts;return e?.[b]||e?.default},j=async()=>{let a=await fetch(`${f}/api/fetch-data/agent-default`),b=await a.json();return{ok:a.ok,json:b}},k=async()=>{let a=await fetch(`${f}/api/fetch-data/recommended-codegpt-models`),b=await a.json();return{ok:a.ok,json:b}}},44725:a=>{function b(a){var b=Error("Cannot find module '"+a+"'");throw b.code="MODULE_NOT_FOUND",b}b.keys=()=>[],b.resolve=b,b.id=44725,a.exports=b},98498:(a,b,c)=>{"use strict";c.d(b,{A:()=>d});let d=function(a){try{a.exec(`
      CREATE TABLE IF NOT EXISTS "connection" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "provider" TEXT NOT NULL UNIQUE,
        "apikey" TEXT,
        "organization_id" TEXT DEFAULT NULL,
        "custom_link" TEXT DEFAULT NULL,
        "google_Oauth" TEXT DEFAULT NULL,
        "region" TEXT DEFAULT NULL,
        "access_key_id" TEXT DEFAULT NULL,
        "secret_access_key" TEXT DEFAULT NULL,
        "session_token" TEXT DEFAULT NULL,
        "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP,
        "updated_at" DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    `),a.exec(`
      CREATE TABLE IF NOT EXISTS "codegpt_session" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "access_token" TEXT NULL,
        "refresh_token" TEXT NULL,
        "expires_at" INTEGER NULL,
        "signed_distinct_id" TEXT DEFAULT NULL,
        "distinct_id" TEXT NULL,
        "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP,
        "updated_at" DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    `),a.exec(`
      CREATE TABLE IF NOT EXISTS "settings" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "provider" TEXT NOT NULL UNIQUE,
        "memory" INTEGER DEFAULT 10,
        "temperature" REAL DEFAULT 0,
        "max_tokens" INTEGER DEFAULT 512,
        "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP,
        "updated_at" DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    `),a.exec(`
      CREATE TABLE IF NOT EXISTS "auto_complete" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "enabled" INTEGER NOT NULL DEFAULT 1,
        "provider" TEXT DEFAULT "CodeGPT Plus Beta",
        "model" TEXT DEFAULT "Plus",
        "max_tokens" INTEGER DEFAULT 300,
        "delay" INTEGER DEFAULT 300,
        "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP,
        "updated_at" DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    `),a.exec(`
      CREATE TABLE IF NOT EXISTS "auto_select" (
      "id" INTEGER PRIMARY KEY AUTOINCREMENT,
      "enabled" INTEGER NOT NULL DEFAULT 1,
      "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP,
      "updated_at" DATETIME DEFAULT CURRENT_TIMESTAMP    
      );
    `),a.exec(`
      CREATE TABLE IF NOT EXISTS "flags" (
     "id" INTEGER PRIMARY KEY AUTOINCREMENT,
     "name" TEXT NOT NULL UNIQUE,
     "used" INTEGER NOT NULL DEFAULT 0,
     "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP,
     "updated_at" DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    `),a.exec(`
      CREATE TABLE IF NOT EXISTS "kv" (
      "key" TEXT PRIMARY KEY,
      "value" TEXT NOT NULL
      );
    `),a.exec(`
      CREATE TABLE IF NOT EXISTS "history" (
        "id" TEXT PRIMARY KEY,
        "name" TEXT DEFAULT NULL,
        "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP,
        "updated_at" DATETIME DEFAULT CURRENT_TIMESTAMP
      );
    `),a.exec(`
      CREATE TABLE IF NOT EXISTS "message" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "content" TEXT NOT NULL,
        "role" TEXT NOT NULL,
        "display" TEXT NOT NULL,
        "message_index" INTEGER NOT NULL,
        "history_id" TEXT DEFAULT NULL,
        "created_at" DATETIME DEFAULT CURRENT_TIMESTAMP,
        "updated_at" DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(history_id) REFERENCES history(id),
        UNIQUE(history_id, message_index)
        );
    `),a.exec(`
      CREATE TABLE IF NOT EXISTS "file_hashes" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "origin_file" TEXT NOT NULL,
        "workspace_id" TEXT NOT NULL,
        "hash" TEXT NOT NULL
        );
    `)}catch(a){throw console.error(`Error initializing schema: ${a.message}`),a}}}};
//# sourceMappingURL=8550.js.map