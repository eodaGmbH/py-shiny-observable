import { Runtime, Inspector } from "@observablehq/runtime";

function createCellNode(el) {
  const node = document.createElement("div");
  el.appendChild(node);
  return node;
}

function redefineCells(main, payload) {
  for (const [key, value] of Object.entries(payload.data)) {
    console.log("redefine", key);
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
      let i = -1;
      const main = runtime.module(define, (name) => {
        i++;
        console.log("cell", name, i);
        if (
          payload.cells == null || // include entire notebook
          payload.cells.includes(name) ||
          payload.cells.includes(i)
        ) {
          console.log("embed cell");
          return new Inspector(createCellNode(el));
        }

        return true;
      });

      redefineCells(main, payload);
      addShinyMessageHandler(el, main);
    });
  }
}

Shiny.outputBindings.register(
  new ObservableOutputBinding(),
  "shiny-observable-output",
);
