const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let currentTool = 'pencil';
let isDrawing = false;
let lastX = 0, lastY = 0;

function saveHistory() { /* history logic */ }

function setTool(tool) {
    currentTool = tool;
    document.querySelectorAll('.tool-btn').forEach(b => b.classList.remove('active'));
    event.currentTarget.classList.add('active');
}

function getPos(e) {
    const rect = canvas.getBoundingClientRect();
    return { x: e.clientX - rect.left, y: e.clientY - rect.top };
}

// Drawing
canvas.addEventListener('mousedown', e => { isDrawing = true; const pos = getPos(e); lastX = pos.x; lastY = pos.y; });
canvas.addEventListener('mousemove', e => {
    if (!isDrawing) return;
    const pos = getPos(e);
    ctx.strokeStyle = currentTool === 'eraser' ? '#fff' : '#111';
    ctx.lineWidth = currentTool === 'eraser' ? 35 : 7;
    ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(pos.x, pos.y);
    ctx.stroke();
    lastX = pos.x; lastY = pos.y;
});
canvas.addEventListener('mouseup', () => isDrawing = false);

// Generation
async function generateDesign() {
    const prompt = document.getElementById('prompt').value || "futuristic design";
    const container = document.getElementById('generatedDesigns');
    
    container.innerHTML = `<div class="flex flex-col items-center py-20"><div class="animate-spin w-12 h-12 border-4 border-purple-500 border-t-transparent rounded-full"></div><p class="mt-6 text-purple-400">Generating studio quality design...</p></div>`;
    
    await new Promise(r => setTimeout(r, 1600));
    
    container.innerHTML = `<div onclick="applyDesign()" class="cursor-pointer bg-gradient-to-br from-zinc-900 to-black p-6 rounded-3xl border border-purple-500/50"><p class="font-medium">${prompt}</p><p class="text-xs text-purple-400">Click to apply to canvas</p></div>`;
}

function applyDesign() {
    ctx.fillStyle = '#111';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#c026d3';
    ctx.font = 'bold 140px Space Grotesk';
    ctx.fillText('APEX', 180, 380);
    alert("Design applied successfully!");
}

function loadPreset(btn) {
    document.getElementById('prompt').value = btn.textContent;
    generateDesign();
}

// Init
ctx.fillStyle = '#fafafa';
ctx.fillRect(0, 0, canvas.width, canvas.height);
