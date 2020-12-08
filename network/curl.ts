const url_ = Deno.args[0];
const res = await fetch(url_);

const body = new Uint8Array(await res.arrayBuffer());
await Deno.stdout.write(body);