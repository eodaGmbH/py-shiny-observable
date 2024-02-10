import { Runtime, Inspector } from "@observablehq/runtime";

class ObservableOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-observable-output");
  }

  renderValue(el, payload) {
    console.log(payload);
    el.style.width = payload.width;
    let main = (window.obsMain = "test");
    const nb = payload.notebook;
    import(nb).then((module) => {
      // console.log(module);
      const define = module.default;
      const runtime = new Runtime();
      // Embed complete notebook
      if (payload.cells == null) {
        main = runtime.module(define, Inspector.into(el));
      } else {
        // embed single cell
        main = runtime.module(define, (name) => {
          console.log("cell", name);
          if (name === payload.cells[0]) {
            console.log("embed me");
            return new Inspector(el);
          }
          // return 1;
        });
        console.log("main here", main);
      }
    });
    console.log("main", main);
  }
}

Shiny.outputBindings.register(
  new ObservableOutputBinding(),
  "shiny-observable-output",
);
