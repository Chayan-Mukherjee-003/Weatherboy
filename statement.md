# Weatherboy - Project Statement

## Problem Statement

In today's digital age, weak passwords are one of the leading causes of security breaches and unauthorized access to personal accounts. Many users create passwords that are easy to remember but also easy to crack, making them vulnerable to cyber attacks. There is a need for a simple tool that can evaluate password strength and help users create secure passwords that follow industry best practices.

## Scope of the Project

This project aims to develop a command-line based Password Strength Checker and Generator application using Python. The system will analyze user-provided passwords against multiple security criteria and provide instant feedback on password strength. Additionally, it will offer a password generation feature that creates strong, secure passwords automatically.

The project focuses on implementing core password security evaluation logic and providing an interactive user interface for easy access to both checking and generating passwords.

## Inclusions (What the system does)

1. **Password Strength Analysis**
   - Evaluates passwords based on length (minimum 8 characters)
   - Checks for presence of uppercase letters
   - Checks for presence of lowercase letters
   - Checks for presence of numeric digits
   - Checks for presence of special characters
   - Assigns a strength score (0-6 points)
   - Categorizes passwords as WEAK, MEDIUM, or STRONG

2. **Feedback and Suggestions**
   - Displays visual strength indicator using progress bars
   - Provides specific suggestions for improving weak passwords
   - Lists missing password criteria

3. **Password Generation**
   - Generates secure passwords with customizable length
   - Ensures inclusion of all character types (uppercase, lowercase, digits, special characters)
   - Automatically verifies generated password strength

4. **User Interface**
   - Interactive menu-driven system
   - Clear input prompts and output displays
   - Easy navigation between features

## Target Users

- **General Computer Users**: Individuals who want to verify if their passwords are secure
- **Students**: Learning about password security and best practices
- **IT Enthusiasts**: People interested in cybersecurity fundamentals
- **Organizations**: Small teams needing a simple password policy enforcement tool
- **Developers**: Those looking to understand password validation logic

## High-Level Features

1. **Real-time Password Evaluation**: Instant analysis of password strength with detailed scoring
2. **Visual Strength Indicator**: Graphical representation of password security level
3. **Intelligent Suggestions**: Context-aware recommendations for password improvement
4. **Custom Password Generation**: Flexible password creation with user-defined length
5. **Pattern-based Generation**: Ensures diversity in generated passwords
6. **No External Dependencies**: Runs with Python standard library only
7. **Cross-platform Compatibility**: Works on Windows, Mac, and Linux systems
8. **User-friendly Interface**: Simple menu system for easy navigation