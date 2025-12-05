/**
 * NoizyButton Component (Mobile)
 * ==============================
 * Styled button matching NoizyFlow design.
 */

import React from "react";
import { TouchableOpacity, Text, StyleSheet, ActivityIndicator } from "react-native";

export default function NoizyButton({ 
  label, 
  onPress, 
  danger = false, 
  calm = false,
  disabled = false,
  loading = false,
  style = {}
}) {
  const bgColor = 
    disabled ? "#333" :
    danger ? "#FF3747" :
    calm ? "#00E5FF" :
    "#F5C542";

  const textColor = 
    disabled ? "#666" :
    "#000000";

  return (
    <TouchableOpacity
      style={[
        styles.button,
        { backgroundColor: bgColor },
        style
      ]}
      onPress={onPress}
      disabled={disabled || loading}
      activeOpacity={0.7}
    >
      {loading ? (
        <ActivityIndicator color={textColor} />
      ) : (
        <Text style={[styles.text, { color: textColor }]}>
          {label}
        </Text>
      )}
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  button: {
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 8,
    marginVertical: 8,
    alignItems: "center",
    justifyContent: "center",
    minHeight: 50
  },
  text: {
    fontSize: 16,
    fontWeight: "bold",
    letterSpacing: 0.5
  }
});

