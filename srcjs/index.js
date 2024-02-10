import { Runtime, Inspector } from "@observablehq/runtime";

function createCellNode(el, name) {
  const node = document.createElement("div");
  node.id = `observable-${el.id}-${name}`;
  console.log(node.id);
  el.appendChild(node);
  return node;
}

function redefineCells(main, payload) {
  for (const [key, value] of Object.entries(payload.data)) {
    console.log(key, value);
    main.redefine(key, value);
  }
}

function addShinyMessageHandler(el, main) {
  const messageHandlerName = `observable-${el.id}`;
  console.log(messageHandlerName);
  Shiny.addCustomMessageHandler(messageHandlerName, (payload) => {
    console.log(payload);
    redefineCells(main, payload);
  });
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
        let i = -1;
        main = runtime.module(define, (name) => {
          i++;
          console.log("cell", name, i);
          if (payload.cells.includes(name) || payload.cells.includes(i)) {
            console.log("embed me");
            // return new Inspector(el);
            return new Inspector(createCellNode(el, name));
          }
          return true;
        });
        console.log("main", main);
        for (const [key, value] of Object.entries(payload.data)) {
          console.log(key, value);
          main.redefine(key, value);
        }
        addShinyMessageHandler(el, main);
      }
    });
  }
}

Shiny.outputBindings.register(
  new ObservableOutputBinding(),
  "shiny-observable-output",
);
