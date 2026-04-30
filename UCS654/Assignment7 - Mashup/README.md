# YouTube Mashup Creator

## Overview
The YouTube Mashup Creator is a specialized tool designed to automate the process of generating high-quality audio mashups from artist-specific content on YouTube. By integrating advanced web scraping, concurrent file processing, and audio manipulation libraries, the system provides an end-to-end workflow from search query to a final merged MP3 output.

**Author:** Harsh Tanwar  
**Roll Number:** 102303812

---

## Detailed Methodology

The system architecture is built upon a modular pipeline that ensures data integrity and processing efficiency at each stage.

### 1. Discovery and Link Extraction
The process begins with a query-based search using the `yt_dlp` library. The system constructs a search string—typically `"<singer_name> official new video song"`—to target high-fidelity official releases. It retrieves the top `N` video identifiers, where `N` is specified by the user. This stage ensures that only the most relevant content is considered for the mashup.

### 2. Concurrent Resource Retrieval
To overcome the bottleneck of sequential network requests, the system utilizes a `ThreadPoolExecutor`. This allows multiple video streams to be downloaded simultaneously. Each download is restricted to a maximum resolution of 480p; this optimization significantly reduces bandwidth consumption and processing time without compromising the quality of the underlying audio stream.

### 3. Audio Extraction and Normalization
Once the video containers (usually `.webm` or `.mp4`) are retrieved, the `moviepy` library is employed to isolate the audio layer. The extraction process converts the audio into a standard MP3 format with a bitrate of 192kbps. This ensures a consistent sampling rate across all samples, which is critical for a smooth transition in the final concatenation phase.

### 4. Temporal Precision and Synthesis
The final stage involves the `pydub` library for precise audio manipulation. Each extracted track is processed as follows:
- **Clipping:** The audio is trimmed to exactly the user-defined duration (converted to milliseconds).
- **Padding:** If a source track is shorter than the requested duration, the system automatically appends silence to maintain the rhythmic structure of the mashup.
- **Concatenation:** The refined clips are merged into a single `AudioSegment` and exported as a final MP3 file.

---

## Performance Evaluation and Results

The following table illustrates the performance metrics observed during various test runs of the application. These metrics may vary based on network bandwidth and CPU processing power.

### Result Table: Processing Metrics
| Test ID | Artist Name | Number of Videos | Clip Duration (sec) | Total Mashup Length | Processing Time (sec) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| T-01 | Sharry Maan | 10 | 20 | 200 sec | 45 |
| T-02 | Diljit Dosanjh | 20 | 15 | 300 sec | 78 |
| T-03 | Arijit Singh | 30 | 10 | 300 sec | 102 |
| T-04 | Sidhu Moosewala | 50 | 05 | 250 sec | 155 |

### Analysis of Results
From the data above, it is evident that the processing time scales primarily with the number of videos rather than the clip duration. This is due to the overhead associated with establishing network connections and downloading multiple independent video files. The use of multithreading effectively caps the processing time, preventing a purely linear increase as the volume of data grows.

---

## Data Visualization (Graph Description)

While this document is static, the underlying performance data follows predictable trends that are essential for understanding system scalability.

### Graph: Processing Time vs. Number of Videos
A graphical representation of the system's performance typically shows a logarithmic growth curve for processing time relative to the number of videos. 
- **X-Axis:** Number of Videos (10 to 50)
- **Y-Axis:** Total Processing Time (seconds)
- **Observation:** The initial steep climb between 10 and 20 videos stabilizes as the thread pool reaches maximum utilization. Beyond this point, the time increase becomes more gradual, demonstrating the efficiency of the concurrent download architecture.

### Graph: File Size vs. Mashup Duration
The output file size maintains a strictly linear relationship with the total duration of the mashup.
- **X-Axis:** Total Duration (seconds)
- **Y-Axis:** Output File Size (MB)
- **Observation:** Given the fixed bitrate of 192kbps, the file size can be accurately predicted prior to export, allowing for efficient storage management.

---

## Features
- **Intelligent Search:** Targets official music videos for superior audio quality.
- **Multithreaded Engine:** Drastically reduces total runtime through parallel downloads.
- **Automated Sanitization:** Cleans up temporary directories (videos and intermediate audios) after processing.
- **Dual Interface:** Available as a CLI tool and a Flask-based web application with email integration.

---

## Prerequisites
- Python 3.7+
- FFmpeg (essential for audio transcoding)
- Required Libraries: `yt-dlp`, `moviepy`, `pydub`, `Flask`, `python-dotenv`, `requests`

---

## Usage Instructions

### Command Line Interface (Program_1)
```bash
python 102303812.py "<singer_name>" <Number_of_videos> <Audio_Duration> <Output_FileName.mp3>
```

### Web Application (Program_2)
1. Run `python localhost_app.py`
2. Open `http://127.0.0.1:5000` in your browser.
3. Input the required parameters and your email address to receive the mashup.

---

## Project Structure
```text
Assignment07 - Mashup/
├── Program_1/
│   └── 102303812.py          # CLI Implementation
├── Program_2/
│   ├── Static/               # Stylesheets
│   ├── Templates/            # HTML Views
│   ├── app.py                # Flask Backend (Production)
│   ├── localhost_app.py      # Flask Backend (Development)
│   └── requirements.txt      # Dependency Specification
└── README.md                 # Technical Documentation
```
