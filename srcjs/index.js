import { Runtime, Inspector } from "@observablehq/runtime";

function createCellNode(el, name) {
  const node = document.createElement("div");
  node.id = `observable-${el.id}-${name}`;
  console.log(node.id);
  el.appendChild(node);
  return node;
}

class ObservableOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-observable-output");
  }

  renderValue(el, payload) {
    console.log(payload);
    el.style.width = payload.width;
    const nb = payload.notebook;

    // Import nb
    import(nb).then((module) => {
      const define = module.default;
      const runtime = new Runtime();
      let main;

      // Embed complete notebook
      if (payload.cells == null) {
        main = runtime.module(define, Inspector.into(el));

        // Embed single cell
      } else {
        main = runtime.module(define, (name) => {
          console.log("cell", name);
          if (payload.cells.includes(name)) {
            console.log("embed me");
            // return new Inspector(el);
            return new Inspector(createCellNode(el, name));
          }
        });
        console.log("main", main);
      }
    });
  }
}

Shiny.outputBindings.register(
  new ObservableOutputBinding(),
  "shiny-observable-output",
);
