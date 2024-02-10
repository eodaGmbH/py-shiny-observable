import { Runtime, Inspector } from "@observablehq/runtime";

class ObservableOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-observable-output");
  }

  renderValue(el, payload) {
    console.log(payload);
    el.style.width = payload.width;

    const nb = payload.notebook;
    import(nb).then((module) => {
      // console.log(module);
      const define = module.default;
      const runtime = new Runtime();
      const main = runtime.module(define, Inspector.into(el));
    });
  }
}

Shiny.outputBindings.register(
  new ObservableOutputBinding(),
  "shiny-observable-output",
);
