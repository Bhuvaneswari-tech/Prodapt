export type MenuItem = {
  id: string;
  name: string;
  priceCents: number;
};

export type MenuState = {
  status: "idle" | "loading" | "success" | "error";
  restaurantId: string | null;
  items: MenuItem[];
  fetchedAt: number | null;
  error: string | null;
};