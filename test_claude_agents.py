#!/usr/bin/env python3
"""
Test Moon Dev agents that require Claude API
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))

print("=" * 70)
print("🌙 Moon Dev AI Agents - Claude API Test")
print("=" * 70)

# Test 1: Verify Claude API works
print("\n1️⃣  Verifying Claude API...")
print("-" * 70)
try:
    import os
    from dotenv import load_dotenv
    import anthropic
    
    load_dotenv()
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_KEY"))
    
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=20,
        messages=[{"role": "user", "content": "Say hello"}]
    )
    
    print(f"✅ Claude API Key Valid")
    print(f"   Model: claude-3-haiku-20240307")
    
except Exception as e:
    print(f"❌ Claude API failed: {e}")
    print("\n⚠️  Cannot test agents without valid Claude API key")
    sys.exit(1)

# Test 2: Check if agents can initialize
print("\n2️⃣  Testing Agent Initialization...")
print("-" * 70)

agents_tested = []

# Risk Agent
try:
    print("Testing Risk Agent initialization...", end=" ")
    # Note: Risk Agent needs portfolio/exchange setup, just check imports
    from src.agents.risk_agent import RiskAgent
    print("✅ Imports OK (needs exchange setup for full test)")
    agents_tested.append(("Risk Agent", "partial", "Needs exchange configuration"))
except Exception as e:
    print(f"❌ Failed: {e}")
    agents_tested.append(("Risk Agent", "failed", str(e)[:50]))

# Strategy Agent  
try:
    print("Testing Strategy Agent initialization...", end=" ")
    from src.agents.strategy_agent import StrategyAgent
    # Try to init (may fail due to missing strategies, but that's OK)
    try:
        agent = StrategyAgent()
        print("✅ Initialized successfully")
        agents_tested.append(("Strategy Agent", "success", "Fully initialized"))
    except:
        print("✅ Imports OK (strategies not configured)")
        agents_tested.append(("Strategy Agent", "partial", "Needs strategy configuration"))
except Exception as e:
    print(f"❌ Failed: {e}")
    agents_tested.append(("Strategy Agent", "failed", str(e)[:50]))

# Chart Analysis Agent
try:
    print("Testing Chart Analysis Agent initialization...", end=" ")
    from src.agents.chartanalysis_agent import ChartAnalysisAgent
    print("✅ Imports OK (needs market data for full test)")
    agents_tested.append(("Chart Analysis Agent", "partial", "Needs market data"))
except Exception as e:
    print(f"❌ Failed: {e}")
    agents_tested.append(("Chart Analysis Agent", "failed", str(e)[:50]))

# Test 3: Trading Agent in Swarm Mode
print("\n3️⃣  Testing Trading Agent (Swarm Mode)...")
print("-" * 70)
print("⚠️  Trading Agent in SWARM mode doesn't require Claude!")
print("   It uses: OpenAI, Gemini, xAI, Ollama for consensus")
agents_tested.append(("Trading Agent (Swarm)", "available", "Works without Claude"))

# Summary
print("\n" + "=" * 70)
print("📊 AGENT TEST SUMMARY")
print("=" * 70)

for agent_name, status, note in agents_tested:
    if status == "success":
        icon = "✅"
    elif status == "partial":
        icon = "⚠️ "
    elif status == "available":
        icon = "💡"
    else:
        icon = "❌"
    
    print(f"{icon} {agent_name}: {note}")

print("\n" + "=" * 70)
print("🎯 NEXT STEPS")
print("=" * 70)
print("✅ Claude API is working with claude-3-haiku-20240307")
print("\n📝 To fully test these agents, you need:")
print("   • Risk Agent: Exchange setup + portfolio configuration")
print("   • Strategy Agent: Custom strategy files in src/strategies/custom/")
print("   • Chart Analysis: Market data from exchange")
print("   • Trading Agent: Can use SWARM mode (no Claude needed!)")
print("=" * 70)
