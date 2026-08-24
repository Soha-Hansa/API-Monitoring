## AI-Powered API Reliability Copilot — Project Description

The **AI-Powered API Reliability Copilot** is a real-time API monitoring and AI-assisted incident analysis system. Its main purpose is to help developers quickly understand when an API becomes unhealthy, why the problem may be happening, how serious it is, and what actions should be taken.

### 🔹 How the project works

The system continuously monitors registered APIs and selected dependencies such as **Redis**.

**Workflow:**

`Monitor → Collect Metrics → Detect Problem → Create Incident → AI Analysis → Recommendation → Dashboard`

It collects information such as:

- API health/status
- Response time / latency
- Request rate
- Error rate
- Redis traffic
- Redis latency
- Redis connections
- Redis memory usage

When predefined thresholds or abnormal patterns are detected, the system automatically creates an **incident**. The AI then analyzes the incident data and provides a probable cause, severity, explanation, and recommended actions.

### 🔹 Problems it detects

The first version focuses on five major incident types:

1. **API Down** — API cannot be reached.
2. **High Latency** — API response time becomes too high.
3. **Error Spike** — failed requests suddenly increase.
4. **Traffic Spike** — request volume becomes unusually high.
5. **Dependency Problem** — Redis and API metrics indicate a possible dependency-related degradation.
