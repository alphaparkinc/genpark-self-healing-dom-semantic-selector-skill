from client import SelfHealingDomSemanticSelectorClient

def main():
    client = SelfHealingDomSemanticSelectorClient()
    res = client.resolve_target_element('Login Button')
    print('Self-Healing DOM Selector: ' + res['resolution_id'] + ' (Confidence: ' + str(res['confidence_score'] * 100) + '%)')
    print('Healed Selector: ' + res['healed_selector'] + ' | Drift: ' + res['drift_cause'])
    print('Telemetry URL: ' + res['selector_telemetry_url'])

if __name__ == '__main__':
    main()
