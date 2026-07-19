const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 1600,
    height: 1000,
    webPreferences: { nodeIntegration: false }
  });
  win.loadFile('index.html');
}

app.whenReady().then(createWindow);
