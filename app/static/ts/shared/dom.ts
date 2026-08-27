/*
- export: makes it importable
- T: ensures that it conforms to Element
- types are explicitly shown like how its done in python
*/
export function requireElement<T extends Element>(selector: string): T { 
    const element = document.querySelector<T>(selector);

    if (!element) {
        throw new Error("Missing required element."); // exists early
    }

    return element;
}