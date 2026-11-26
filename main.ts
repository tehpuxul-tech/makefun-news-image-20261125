// A news-image entry for make.fun (Node 22, standard library only).
// The entry image sits beside this file as entry.png; the program copies
// it to the harness output directory so the grader sees exactly those
// bytes. Run it locally with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
copyFileSync(new URL("./entry.png", import.meta.url), join(outDir, "entry.png"));
