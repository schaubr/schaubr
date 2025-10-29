#!/usr/bin/env python3
"""
AI Service Recommendation Flow - Runner Script

Dit script laat toe om de LangFlow flow programmatisch uit te voeren.
"""

import os
import json
import requests
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class ServiceRecommendationFlow:
    """Wrapper voor de AI Service Recommendation Flow"""

    def __init__(self, langflow_url: str = None, api_token: str = None):
        """
        Initialiseer de flow runner

        Args:
            langflow_url: URL van de LangFlow instantie
            api_token: API token voor authenticatie (optioneel)
        """
        self.langflow_url = langflow_url or os.getenv('LANGFLOW_API_URL', 'http://localhost:7860')
        self.api_token = api_token or os.getenv('LANGFLOW_API_TOKEN')
        self.flow_id = None

    def load_flow(self, flow_path: str = 'ai_service_recommendation_flow.json'):
        """Laad de flow definitie"""
        with open(flow_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def run_flow(self, customer_context: str, problem_description: str) -> Dict[str, Any]:
        """
        Voer de flow uit met de gegeven inputs

        Args:
            customer_context: Beschrijving van de klantcontext
            problem_description: Beschrijving van de problematiek

        Returns:
            Dict met het gegenereerde voorstel en metadata
        """
        # Prepare the request payload
        payload = {
            "inputs": {
                "customer_context": customer_context,
                "problem_description": problem_description
            }
        }

        # Add authentication header if token is available
        headers = {}
        if self.api_token:
            headers['Authorization'] = f'Bearer {self.api_token}'

        # Make the request to LangFlow API
        try:
            response = requests.post(
                f"{self.langflow_url}/api/v1/run/{self.flow_id}",
                json=payload,
                headers=headers,
                timeout=300  # 5 minute timeout for complex flows
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error running flow: {e}")
            raise

    def run_flow_cli(self):
        """Interactieve CLI voor het runnen van de flow"""
        print("=" * 80)
        print("AI Service Recommendation Flow - Interactieve Modus")
        print("=" * 80)
        print()

        print("Klant Context:")
        print("Beschrijf de klantcontext (industrie, bedrijfsgrootte, uitdagingen, etc.)")
        print("Druk op Enter twee keer om te eindigen:")

        customer_context_lines = []
        while True:
            line = input()
            if line == "" and customer_context_lines and customer_context_lines[-1] == "":
                break
            customer_context_lines.append(line)
        customer_context = "\n".join(customer_context_lines[:-1])

        print("\nProbleem Beschrijving:")
        print("Beschrijf de specifieke problematiek en behoeften:")
        print("Druk op Enter twee keer om te eindigen:")

        problem_lines = []
        while True:
            line = input()
            if line == "" and problem_lines and problem_lines[-1] == "":
                break
            problem_lines.append(line)
        problem_description = "\n".join(problem_lines[:-1])

        print("\n" + "=" * 80)
        print("Flow wordt uitgevoerd...")
        print("=" * 80)

        result = self.run_flow(customer_context, problem_description)

        print("\n" + "=" * 80)
        print("RESULTAAT")
        print("=" * 80)
        print()

        if 'outputs' in result:
            if 'final_output' in result['outputs']:
                print("VOORSTEL:")
                print("-" * 80)
                print(result['outputs']['final_output'])
                print()

            if 'metadata_output' in result['outputs']:
                print("\nMETADATA:")
                print("-" * 80)
                print(json.dumps(result['outputs']['metadata_output'], indent=2, ensure_ascii=False))
        else:
            print(json.dumps(result, indent=2, ensure_ascii=False))


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Run the AI Service Recommendation Flow'
    )
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Run in interactive mode'
    )
    parser.add_argument(
        '--customer-context', '-c',
        type=str,
        help='Customer context (alternatively use --context-file)'
    )
    parser.add_argument(
        '--problem', '-p',
        type=str,
        help='Problem description (alternatively use --problem-file)'
    )
    parser.add_argument(
        '--context-file',
        type=str,
        help='Path to file containing customer context'
    )
    parser.add_argument(
        '--problem-file',
        type=str,
        help='Path to file containing problem description'
    )
    parser.add_argument(
        '--output', '-o',
        type=str,
        help='Output file path (default: stdout)'
    )

    args = parser.parse_args()

    # Initialize the flow runner
    runner = ServiceRecommendationFlow()

    # Interactive mode
    if args.interactive:
        runner.run_flow_cli()
        return

    # File or argument mode
    customer_context = args.customer_context
    if args.context_file:
        with open(args.context_file, 'r', encoding='utf-8') as f:
            customer_context = f.read()

    problem_description = args.problem
    if args.problem_file:
        with open(args.problem_file, 'r', encoding='utf-8') as f:
            problem_description = f.read()

    if not customer_context or not problem_description:
        print("Error: Either use --interactive mode or provide both customer context and problem description")
        parser.print_help()
        return

    # Run the flow
    result = runner.run_flow(customer_context, problem_description)

    # Output results
    output_data = json.dumps(result, indent=2, ensure_ascii=False)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output_data)
        print(f"Results written to {args.output}")
    else:
        print(output_data)


if __name__ == '__main__':
    main()
