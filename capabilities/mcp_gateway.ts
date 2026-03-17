/**
 * MCP Gateway server
 * Model Context Protocol simple implementation bridging TickTick and other services
 */
// @ts-ignore - Ignore module resolution for bare-metal deploy
import express from 'express';

const app = express();
app.use(express.json());

// Simulated dependencies
// @ts-ignore - Ignore process definition
const TICKTICK_CLIENT_ID = process.env.TICKTICK_CLIENT_ID;

// Mock implementations for demonstration purposes

app.post('/api/tools/ticktick_add_task', (req: any, res: any) => {
    const { name, date, project_id, priority } = req.body;
    console.log(`[MCP TickTick] Adding task: ${name} to project ${project_id} at ${date} [Pri:${priority}]`);
    res.json({ success: true, taskId: `ttk_${Date.now()}` });
});

app.post('/api/tools/ticktick_get_today', (req: any, res: any) => {
    console.log(`[MCP TickTick] Fetching today's tasks...`);
    res.json({ 
        success: true, 
        tasks: [
            { id: "ttk_01", title: "Review WappTV Routes", status: "pending" }
        ]
    });
});

app.post('/api/tools/youtube_search', (req: any, res: any) => {
    const { query } = req.body;
    console.log(`[MCP YouTube] Searching for: ${query}`);
    res.json({ success: true, results: ["http://youtube.com/watch?v=mock"] });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`MCP Gateway listening correctly on port ${PORT}`);
});
