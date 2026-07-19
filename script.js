const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

let currentTool = 'pencil';
let isDrawing = false;
let lastX = 0, lastY = 0;

// Set tool
function setTool(tool) {
  currentTool = tool;
  document.querySelectorAll('.tool-btn').forEach(btn => btn.classList.remove('active'));
}

// Drawing
canvas.addEventListener('mousedown', (e) => {
  isDrawing = true;
  const rect = canvas.getBoundingClientRect();
  lastX = e.clientX - rect.left;
  lastY = e.clientY - rect.top;
});

canvas.addEventListener('mousemove', (e) => {
  if (!isDrawing) return;
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;

  ctx.strokeStyle = currentTool === 'eraser' ? '#ffffff' : '#000000';
  ctx.lineWidth = currentTool === 'eraser' ? 30 : 8;
  ctx.lineCap = 'round';

  ctx.beginPath();
  ctx.moveTo(lastX, lastY);
  ctx.lineTo(x, y);
  ctx.stroke();

  lastX = x;
  lastY = y;
});

canvas.addEventListener('mouseup', () => isDrawing = false);
canvas.addEventListener('mouseout', () => isDrawing = false);

// Generate Design
function generateDesign() {
  alert("Design generation started! (Canvas will be updated)");
  ctx.fillStyle = "#f0f0f0";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#8b00ff";
  ctx.font = "bold 100px Arial";
  ctx.fillText("APEX", 300, 400);
}

// Init canvas
ctx.fillStyle = "#ffffff";
ctx.fillRect(0, 0, canvas.width, canvas.height);
