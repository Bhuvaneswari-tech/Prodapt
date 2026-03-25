import React from "react";
import { UIProvider } from "./ui/UIContext";
import { AuthProvider } from "./auth/AuthContext";
import { MenuProvider } from "./menu/MenuContext";
import { CartProvider } from "./cart/CartContext";
import { OrderProvider } from "./order/OrderContext";

export function AppProviders({ children }: { children: React.ReactNode }) {
  return (
    <UIProvider>
      <AuthProvider>
        <MenuProvider>
          <CartProvider>
            <OrderProvider>{children}</OrderProvider>
          </CartProvider>
        </MenuProvider>
      </AuthProvider>
    </UIProvider>
  );
}