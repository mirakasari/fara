import SwiftUI
import MapKit

struct PassportView: View {
    @State private var position: MapCameraPosition = .automatic

    var body: some View {
        NavigationStack {
            VStack {
                Map(position: $position)
                    .frame(minHeight: 300)
                    .clipShape(RoundedRectangle(cornerRadius: 12))
                List {
                    Section("Visited") {
                        Text("No countries logged yet")
                            .italic()
                    }
                }
            }
            .navigationTitle("Passport")
            .toolbar {
                Button {
                    // Placeholder action
                } label: {
                    Label("Add", systemImage: "plus")
                }
            }
        }
    }
}

#Preview {
    PassportView()
}
