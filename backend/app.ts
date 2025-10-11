import express, { Request, Response } from "express";
import cors from "cors";

const app = express();
const PORT = 4000;

app.use(cors());
app.use(express.json());

// Health check endpoint
app.get("/api/health", (req: Request, res: Response) => {
    res.json({ status: "OK" });
});

app.listen(PORT, () => console.log(`Backend running on http://localhost:${PORT}`));
