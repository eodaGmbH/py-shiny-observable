function createCellNode(el) {
  const node = document.createElement("div");
  el.appendChild(node);
  return node;
}

export { createCellNode };
