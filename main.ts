// Entry program for news-image-20261126.
// Copies the bundled entry.png to the output directory.
// Runs with no network and the Node standard library only.
import { copyFileSync, existsSync, mkdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
const dest = join(outDir, "entry.png");

if (!existsSync(source)) {
  throw new Error("entry.png is missing from the repository");
}

const size = statSync(source).size;
if (size <= 0 || size > 1048576) {
  throw new Error(`entry.png size ${size} is outside the allowed range`);
}

const bytes = readFileSync(source);
const head = bytes.subarray(0, 8);
const isPng =
  head[0] === 0x89 && head[1] === 0x50 && head[2] === 0x4e && head[3] === 0x47;
if (!isPng) {
  throw new Error("entry.png is not a PNG file");
}

// PNG IHDR: width and height are big-endian uint32 at bytes 16..23.
const width = bytes.readUInt32BE(16);
const height = bytes.readUInt32BE(20);
if (width <= 0 || height <= 0 || width > 1024 || height > 1024) {
  throw new Error(`entry.png dimensions ${width}x${height} exceed 1024x1024`);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, dest);
console.log(`wrote ${dest} (${width}x${height}, ${size} bytes)`);
