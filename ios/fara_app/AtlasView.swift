import SwiftUI

struct AtlasView: View {
    var body: some View {
        NavigationStack {
            List {
                Section {
                    NavigationLink("By Country") {
                        List {
                            Text("USA")
                            Text("Italy")
                            Text("Japan")
                        }
                        .navigationTitle("By Country")
                    }
                    NavigationLink("By Cuisine") {
                        List {
                            Text("Italian")
                            Text("Japanese")
                            Text("Mexican")
                        }
                        .navigationTitle("By Cuisine")
                    }
                    NavigationLink("By Dish") {
                        List {
                            Text("Pizza")
                            Text("Sushi")
                            Text("Tacos")
                        }
                        .navigationTitle("By Dish")
                    }
                }
                Section("Featured") {
                    NavigationLink {
                        FoodCardDetailView(
                            title: "Sample Dish",
                            description: "This is a placeholder description for a featured dish. It includes some details about the dish and what makes it special."
                        )
                    } label: {
                        Text("Sample Dish")
                    }
                }
            }
            .navigationTitle("Atlas")
        }
    }
}

private struct FoodCardDetailView: View {
    let title: String
    let description: String
    
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                Text(title)
                    .font(.title)
                    .fontWeight(.bold)
                Text(description)
                    .font(.body)
            }
            .padding()
        }
        .navigationTitle(title)
    }
}

#Preview {
    AtlasView()
}
