/**
 * Wrapper for the OpenViking Context DB API 
 * Uses standard viking:// protocol paths to fetch or write context vectors.
 */

const OPENVIKING_URL = process.env.OPENVIKING_API_URL || 'http://maestro_openviking:8080';

export async function read_path(vikingPath) {
    console.log(`[OpenViking Bridge] Fetching abstract for: ${vikingPath}`);
    // Simulated fetch call to OpenViking Container
    const response = await fetch(`${OPENVIKING_URL}/api/v1/context?uri=${encodeURIComponent(vikingPath)}&tier=L1`);
    if (!response.ok) {
        throw new Error(`Failed to read from OpenViking: ${response.statusText}`);
    }
    return response.json();
}

export async function write_knowledge(vikingDestPath, markdownContent, metadata = {}) {
    console.log(`[OpenViking Bridge] Writing knowledge to: ${vikingDestPath}`);
    // Simulated Post to Context DB
    const payload = {
        uri: vikingDestPath,
        content: markdownContent,
        metadata: metadata
    };
    
    const response = await fetch(`${OPENVIKING_URL}/api/v1/knowledge`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });

    if (!response.ok) {
        throw new Error(`Failed to write to OpenViking: ${response.statusText}`);
    }
    return response.json();
}
