# SportGuard AI: Advanced Anti-Piracy Protection

SportGuard AI is a comprehensive security suite designed to protect live sports broadcasts and premium content from unauthorized distribution. It combines individual stream protection with large-scale network detection.

## Key Features

### 1. Multi-Layer Fingerprinting
Uses four parallel modalities to create a 512-dimensional fused signature:
- **Visual**: Freq-domain analysis (DCT) of keyframes.
- **Audio**: Spectrogram and MFCC characteristic extraction.
- **Temporal**: Mapping scene-change sequences.
- **Semantic**: Gemini AI-driven descriptions of on-screen events.

### 2. Forensic Watermarking
Invisible session-specific watermarking across three domains:
- **Luminance**: DCT mid-frequency coefficient adjustment.
- **Temporal**: Imperceptible frame-timing jitter.
- **Audio**: Phase shifting in high-frequency bands.
- **Payload**: 128-bit structured payload (User, Device, Tier, TS, Region).

### 3. Content Farm & Network Detection
Moves beyond individual leaks to dismantle piracy organizations:
- **Knowledge Graph**: Maps relationships between accounts, IPs, devices, and payments.
- **Pattern Recognition**:
  - **Upload Velocity**: Detects robotic automated posting.
  - **Similarity Clustering**: Grouping accounts by shared content hashing.
  - **Temporal Coordination**: Detecting coordinated schedules across "separate" accounts.
- **Predictive Replacements**: ML models identify new replacement accounts based on historical network patterns.

## Modular Architecture
- `sportguard/fingerprinting/`: Engines for content identification.
- `sportguard/watermarking/`: Forensic embedding and extraction pipelines.
- `sportguard/network/`: Graph analytics and network dismantling protocols.
- `sportguard/attribution/`: Automated response and legal evidence generation.

## System Architecture Diagram

```mermaid
flowchart TD

subgraph group_entry["Entry points"]
  node_main["Main<br/>entrypoint<br/>[main.py]"]
  node_api["API<br/>entrypoint<br/>[api.py]"]
  node_demo["Demo<br/>entrypoint<br/>[demo_sportguard.py]"]
end

subgraph group_ares["ARES layer"]
  node_ares_orchestrator["Orchestrator<br/>workflow<br/>[orchestrator.py]"]
  node_ares_engine["Engine<br/>runtime<br/>[engine.py]"]
  node_ares_ledger[("Ledger<br/>state-store<br/>[ledger.py]")]
  node_ares_models["Models<br/>schema<br/>[models.py]"]
  node_meta_adapter["Meta<br/>adapter<br/>[meta_adapter.py]"]
  node_tiktok_adapter["TikTok<br/>adapter<br/>[tiktok_adapter.py]"]
  node_youtube_adapter["YouTube<br/>adapter<br/>[youtube_adapter.py]"]
  node_external_platforms(("Platforms<br/>external-systems"))
end

subgraph group_sportguard["SportGuard core"]
  node_fp_engine["FP Engine<br/>pipeline<br/>[engine.py]"]
  node_fp_visual["Visual<br/>feature-extractor<br/>[visual.py]"]
  node_fp_audio["Audio<br/>feature-extractor<br/>[audio.py]"]
  node_fp_temporal["Temporal<br/>feature-extractor<br/>[temporal.py]"]
  node_fp_semantic["Semantic<br/>feature-extractor<br/>[semantic.py]"]
  node_fp_fusion["Fusion<br/>signature-fuser<br/>[fusion.py]"]
  node_wm_embedder["Embedder<br/>pipeline<br/>[embedder.py]"]
  node_wm_encoder["Encoder<br/>[encoder.py]"]
  node_wm_luminance["Luminance<br/>watermark-channel<br/>[luminance.py]"]
  node_wm_wt["Timing<br/>watermark-channel<br/>[temporal.py]"]
  node_wm_audio["Audio WM<br/>watermark-channel<br/>[audio.py]"]
  node_net_graph(("Graph<br/>[graph.py]"))
  node_net_detection["Detection<br/>analyzer<br/>[detection.py]"]
  node_net_predictive["Predictive<br/>risk-model<br/>[predictive.py]"]
  node_net_protocol["Protocol<br/>policy<br/>[protocol.py]"]
  node_attr_workflow["Workflow<br/>enforcement-flow<br/>[workflow.py]"]
  node_attr_response["Response<br/>policy-engine<br/>[response.py]"]
  node_content_sources(("Broadcast<br/>source-domain"))
end

subgraph group_evidence["Evidence"]
  node_commercial_evidence["Leaker cases<br/>evidence-store"]
  node_network_evidence["Network case<br/>evidence-store"]
end

node_main -->|"runs"| node_ares_orchestrator
node_api -->|"serves"| node_ares_engine
node_demo -->|"demonstrates"| node_fp_engine
node_ares_orchestrator -->|"coordinates"| node_ares_engine
node_ares_orchestrator -->|"records"| node_ares_ledger
node_ares_engine -->|"normalizes"| node_ares_models
node_ares_engine -->|"ingests"| node_meta_adapter
node_ares_engine -->|"ingests"| node_tiktok_adapter
node_ares_engine -->|"ingests"| node_youtube_adapter
node_meta_adapter -.->|"connects"| node_external_platforms
node_tiktok_adapter -.->|"connects"| node_external_platforms
node_youtube_adapter -.->|"connects"| node_external_platforms
node_external_platforms -.->|"feeds"| node_content_sources
node_content_sources -->|"analyzed by"| node_fp_engine
node_fp_engine -->|"extracts"| node_fp_visual
node_fp_engine -->|"extracts"| node_fp_audio
node_fp_engine -->|"extracts"| node_fp_temporal
node_fp_engine -->|"extracts"| node_fp_semantic
node_fp_visual -->|"fuses"| node_fp_fusion
node_fp_audio -->|"fuses"| node_fp_fusion
node_fp_temporal -->|"fuses"| node_fp_fusion
node_fp_semantic -->|"fuses"| node_fp_fusion
node_wm_embedder -->|"builds"| node_wm_encoder
node_wm_embedder -->|"embeds"| node_wm_luminance
node_wm_embedder -->|"embeds"| node_wm_wt
node_wm_embedder -->|"embeds"| node_wm_audio
node_fp_fusion -->|"correlates"| node_net_graph
node_net_graph -->|"analyzed by"| node_net_detection
node_net_detection -->|"projects"| node_net_predictive
node_net_detection -->|"conforms to"| node_net_protocol
node_net_detection -->|"triggers"| node_attr_workflow
node_attr_workflow -->|"decides"| node_attr_response
node_attr_response -->|"persists"| node_commercial_evidence
node_net_detection -->|"persists"| node_network_evidence
node_attr_response -->|"supports"| node_commercial_evidence

## Getting Started
1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python librosa scipy numpy networkx pandas scikit-learn
   ```
3. Run the demonstration:
   ```bash
   python demo_sportguard.py
   ```

## Automated Response Protocol
- **First-time**: Warning and educational content.
- **Repeat**: Temporary suspension.
- **Commercial Scale**: Permanent termination, evidence preservation, and law enforcement referral.
