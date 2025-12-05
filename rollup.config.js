import svelte from "rollup-plugin-svelte";
import resolve from "@rollup/plugin-node-resolve";
import commonjs from "@rollup/plugin-commonjs";
import terser from '@rollup/plugin-terser';
import typescript from "@rollup/plugin-typescript";
import path from "path";
import fs from "fs";
import postcss from 'rollup-plugin-postcss';
import url from '@rollup/plugin-url';

const production = !process.env.ROLLUP_WATCH;

export default fs
  .readdirSync(path.join(__dirname, "webviews", "pages"))
  .map((input) => {
    const name = input.split(".")[0];

    return {
      input: "webviews/pages/" + input,

      output: {
        sourcemap: true,
        format: "iife",
        name: "app",
        file: "out/compiled/" + name + ".js",
      },

      plugins: [
        svelte({
          compilerOptions: {
            dev: !production,
          },
        }),

        postcss({
          extract: true,  // Ensures CSS files are written separately
          plugins: [
            require("tailwindcss")({
              config: "./tailwind.config.js",
            }),
            require("autoprefixer"),
          ],
        }),

        resolve({
          browser: true,
          dedupe: ["svelte"],
        }),

        commonjs(),

        typescript({
          tsconfig: "webviews/tsconfig.json",
          sourceMap: !production,
          inlineSources: !production,
        }),

        url({
          include: ['**/*.svg', '**/*.png', '**/*.jpg', '**/*.gif'],
          limit: 0, // or set a size limit to inline the files
        }),
        // In dev mode, call `npm run start` once
        // the bundle has been generated
        // !production && serve(),

        // Watch the `public` directory and refresh the
        // browser on changes when not in production
        // !production && livereload("public"),

        // If we're building for production (npm run build
        // instead of npm run dev), minify
        production && terser(),
      ],

      watch: {
        clearScreen: false,
      }
    };
  });