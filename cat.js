for (let i = 0; i < Deno.args.length; i++) {
    const filename = Deno.args[i];
    const file = await Deno.open(filename);
    await Deno.copy(file, Deno.stdout);
    file.close();
  }