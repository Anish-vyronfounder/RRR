import { createFileRoute } from '@tanstack/react-router'
import { useEffect, useRef, useState } from 'react'

export const Route = createFileRoute('/vision-analysis')({ component: VisionAnalysis })

const API_URL = (import.meta.env.VITE_API_URL || 'http://127.0.0.1:8001').replace(/\/$/, '')

function VisionAnalysis() {
  const videoRef = useRef<HTMLVideoElement>(null)
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const streamRef = useRef<MediaStream | null>(null)
  const [cameraOpen, setCameraOpen] = useState(false)
  const [file, setFile] = useState<File | null>(null)
  const [preview, setPreview] = useState<string | null>(null)
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')
  const [result, setResult] = useState<any>(null)

  useEffect(() => () => stopCamera(), [])

  async function startCamera() {
    setError(''); setResult(null)
    try {
      if (!navigator.mediaDevices?.getUserMedia) throw new Error('Camera access is not supported by this browser.')
      const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: { ideal: 'environment' }, width: { ideal: 1280 }, height: { ideal: 720 } }, audio: false })
      streamRef.current = stream
      if (videoRef.current) { videoRef.current.srcObject = stream; await videoRef.current.play() }
      setCameraOpen(true)
    } catch (e: any) {
      setError(e?.name === 'NotAllowedError' ? 'Camera permission was denied. Please allow camera access or upload an image.' : e?.message || 'Unable to start camera.')
    }
  }

  function stopCamera() {
    streamRef.current?.getTracks().forEach(t => t.stop())
    streamRef.current = null
    if (videoRef.current) videoRef.current.srcObject = null
    setCameraOpen(false)
  }

  function capture() {
    const video = videoRef.current, canvas = canvasRef.current
    if (!video || !canvas) return
    canvas.width = video.videoWidth || 1280; canvas.height = video.videoHeight || 720
    canvas.getContext('2d')?.drawImage(video, 0, 0, canvas.width, canvas.height)
    canvas.toBlob(blob => {
      if (!blob) return
      const captured = new File([blob], `rrr-camera-${Date.now()}.jpg`, { type: 'image/jpeg' })
      setFile(captured); setPreview(URL.createObjectURL(blob)); setResult(null); stopCamera()
    }, 'image/jpeg', 0.92)
  }

  function chooseFile(event: React.ChangeEvent<HTMLInputElement>) {
    const selected = event.target.files?.[0]
    if (!selected) return
    setFile(selected); setPreview(URL.createObjectURL(selected)); setResult(null); setError('')
  }

  async function analyze() {
    if (!file) { setError('Capture or upload an image first.'); return }
    setBusy(true); setError(''); setResult(null)
    try {
      const body = new FormData(); body.append('file', file)
      const response = await fetch(`${API_URL}/api/vision/analyze`, { method: 'POST', body })
      const data = await response.json().catch(() => ({}))
      if (!response.ok) throw new Error(data.detail || `Vision API failed (${response.status})`)
      setResult(data)
    } catch (e: any) { setError(e?.message || 'Unable to connect to the RRR backend.') }
    finally { setBusy(false) }
  }

  return <section className="rrr-vision">
    <div className="rrr-card">
      <p className="eyebrow">RRR VISION</p><h1>Identify a chip or component</h1>
      <p>Use your device camera or upload a clear photo. RRR sends both through the same vision API.</p>
      {!cameraOpen ? <div className="actions"><button onClick={startCamera}>📷 Use Camera</button><label className="button secondary">🖼 Upload Image<input hidden type="file" accept="image/jpeg,image/png,image/webp" onChange={chooseFile}/></label></div> : <div className="camera"><video ref={videoRef} playsInline muted/><div className="actions"><button onClick={capture}>Capture</button><button className="secondary" onClick={stopCamera}>Cancel</button></div></div>}
      {preview && <div className="preview"><img src={preview} alt="Selected component"/><button className="secondary" onClick={() => { setFile(null); setPreview(null); setResult(null) }}>Remove</button></div>}
      <canvas ref={canvasRef} hidden />
      <button className="analyze" disabled={!file || busy} onClick={analyze}>{busy ? 'Analyzing…' : 'Analyze Component'}</button>
      {error && <div className="error">{error}</div>}
      {result && <pre className="result">{JSON.stringify(result, null, 2)}</pre>}
    </div>
  </section>
}
