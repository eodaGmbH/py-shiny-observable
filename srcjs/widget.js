class ObservableWidget {
  constructor(el, { notebook, cells, width, data }) {
    el.style.width = width;
    this._el = el;
    this._nb = notebook;
    this._cells = cells;
    this._data = data;
  }
}

export { ObservableWidget };
